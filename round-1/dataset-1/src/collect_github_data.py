#!/usr/bin/env python3
"""
Collect GitHub repository data for OSS survival study.
Collects commit histories, file modifications, and contributor metadata.
"""

from loguru import logger
from pathlib import Path
import json
import sys
import time
import asyncio
import aiohttp
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import random

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

class GitHubDataCollector:
    """Collect GitHub repository data using REST API."""
    
    def __init__(self, token: Optional[str] = None):
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {}
        if token:
            self.headers["Authorization"] = f"token {token}"
        self.headers["Accept"] = "application/vnd.github.v3+json"
        self.rate_limit_remaining = 5000
        self.rate_limit_reset = 0
        
    async def _make_request(self, session: aiohttp.ClientSession, url: str, params: Dict = None) -> Optional[Dict]:
        """Make API request with rate limit handling."""
        while True:
            try:
                async with session.get(url, headers=self.headers, params=params) as response:
                    # Update rate limit info
                    if "X-RateLimit-Remaining" in response.headers:
                        self.rate_limit_remaining = int(response.headers["X-RateLimit-Remaining"])
                    if "X-RateLimit-Reset" in response.headers:
                        self.rate_limit_reset = int(response.headers["X-RateLimit-Reset"])
                    
                    if response.status == 200:
                        return await response.json()
                    elif response.status == 403:
                        # Rate limited
                        reset_time = self.rate_limit_reset - time.time()
                        if reset_time > 0:
                            logger.warning(f"Rate limited. Waiting {reset_time:.0f}s")
                            await asyncio.sleep(min(reset_time + 5, 60))
                            continue
                        else:
                            await asyncio.sleep(60)
                            continue
                    elif response.status == 404:
                        logger.warning(f"Not found: {url}")
                        return None
                    else:
                        logger.error(f"API error {response.status}: {url}")
                        return None
            except Exception as e:
                logger.error(f"Request failed: {e}")
                await asyncio.sleep(5)
                continue
    
    async def search_repositories(self, session: aiohttp.ClientSession, min_stars: int = 100, 
                                  created_before: str = "2024-08-20", pushed_after: str = "2024-02-20",
                                  per_page: int = 100, max_repos: int = 2000) -> List[Dict]:
        """Search for repositories matching criteria."""
        repos = []
        page = 1
        
        # Search query
        query = f"stars:>{min_stars} created:<{created_before} pushed:>{pushed_after}"
        # Add language filter for popular OSS languages
        languages = ["Python", "JavaScript", "Java", "Go", "TypeScript", "C++", "Ruby"]
        
        logger.info(f"Searching for repositories with query: {query}")
        
        for lang in languages[:2]:  # Start with 2 languages to manage API budget
            if len(repos) >= max_repos:
                break
                
            lang_query = f"{query} language:{lang}"
            logger.info(f"Searching language: {lang}")
            
            while len(repos) < max_repos:
                params = {
                    "q": lang_query,
                    "sort": "stars",
                    "order": "desc",
                    "per_page": per_page,
                    "page": page
                }
                
                url = f"{self.base_url}/search/repositories"
                data = await self._make_request(session, url, params)
                
                if not data or "items" not in data:
                    break
                
                items = data["items"]
                if not items:
                    break
                
                repos.extend(items)
                logger.info(f"Collected {len(repos)} repositories so far")
                
                if len(items) < per_page:
                    break
                page += 1
                
                # Check rate limit
                if self.rate_limit_remaining < 10:
                    wait_time = max(0, self.rate_limit_reset - time.time()) + 5
                    logger.warning(f"Low rate limit. Waiting {wait_time:.0f}s")
                    await asyncio.sleep(wait_time)
        
        return repos[:max_repos]
    
    async def get_contributors(self, session: aiohttp.ClientSession, repo_full_name: str) -> List[Dict]:
        """Get repository contributors."""
        url = f"{self.base_url}/repos/{repo_full_name}/contributors"
        params = {"per_page": 100}
        contributors = []
        
        page = 1
        while True:
            params["page"] = page
            data = await self._make_request(session, url, params)
            if not data:
                break
            contributors.extend(data)
            if len(data) < 100:
                break
            page += 1
            await asyncio.sleep(0.1)  # Small delay
        
        return contributors
    
    async def get_commits(self, session: aiohttp.ClientSession, repo_full_name: str, 
                         since: Optional[str] = None, max_commits: int = 500) -> List[Dict]:
        """Get repository commits."""
        url = f"{self.base_url}/repos/{repo_full_name}/commits"
        params = {"per_page": 100}
        if since:
            params["since"] = since
        
        commits = []
        page = 1
        
        while len(commits) < max_commits:
            params["page"] = page
            data = await self._make_request(session, url, params)
            if not data:
                break
            commits.extend(data)
            if len(data) < 100:
                break
            page += 1
            await asyncio.sleep(0.1)
        
        return commits[:max_commits]
    
    async def get_commit_details(self, session: aiohttp.ClientSession, repo_full_name: str, 
                                 commit_sha: str) -> Optional[Dict]:
        """Get detailed commit information including file modifications."""
        url = f"{self.base_url}/repos/{repo_full_name}/commits/{commit_sha}"
        return await self._make_request(session, url)
    
    async def collect_repo_data(self, session: aiohttp.ClientSession, repo: Dict) -> Optional[Dict]:
        """Collect comprehensive data for a single repository."""
        repo_full_name = repo["full_name"]
        logger.info(f"Processing {repo_full_name}")
        
        try:
            # Get contributors
            contributors = await self.get_contributors(session, repo_full_name)
            
            # Get commits (last 2 years)
            two_years_ago = (datetime.now() - timedelta(days=730)).isoformat()
            commits = await self.get_commits(session, repo_full_name, since=two_years_ago)
            
            # Get detailed commit info for top contributors (limit to save API calls)
            top_contributors = contributors[:10] if contributors else []
            commit_details = []
            
            for commit in commits[:50]:  # Limit to 50 commits per repo
                commit_data = await self.get_commit_details(session, repo_full_name, commit["sha"])
                if commit_data and "files" in commit_data:
                    commit_details.append({
                        "sha": commit_data["sha"],
                        "author": commit_data["commit"]["author"]["name"] if commit_data["commit"]["author"] else None,
                        "author_login": commit_data["author"]["login"] if commit_data.get("author") else None,
                        "timestamp": commit_data["commit"]["author"]["date"] if commit_data["commit"]["author"] else None,
                        "message": commit_data["commit"]["message"],
                        "files": [f["filename"] for f in commit_data["files"]],
                        "file_count": len(commit_data["files"])
                    })
            
            # Identify founder (earliest contributor or most commits in first 6 months)
            founder = None
            if contributors:
                # Sort by contributions
                sorted_contribs = sorted(contributors, key=lambda x: x.get("contributions", 0), reverse=True)
                founder = sorted_contribs[0]["login"] if sorted_contribs else None
            
            return {
                "repo_id": repo_full_name,
                "repo_name": repo["name"],
                "repo_owner": repo["owner"]["login"],
                "repo_stars": repo["stargazers_count"],
                "repo_forks": repo["forks_count"],
                "repo_language": repo.get("language"),
                "repo_created": repo["created_at"],
                "repo_last_push": repo["pushed_at"],
                "contributors": [{"login": c["login"], "contributions": c["contributions"]} for c in contributors[:50]],
                "founder": founder,
                "commits": commit_details,
                "commit_count": len(commits)
            }
            
        except Exception as e:
            logger.error(f"Error processing {repo_full_name}: {e}")
            return None
    
    async def collect_data(self, max_repos: int = 100) -> List[Dict]:
        """Main method to collect data from multiple repositories."""
        # Create output directory
        Path("temp/datasets").mkdir(parents=True, exist_ok=True)
        
        async with aiohttp.ClientSession() as session:
            # Search for repositories
            repos = await self.search_repositories(session, max_repos=max_repos)
            logger.info(f"Found {len(repos)} repositories to process")
            
            # Collect data for each repo
            results = []
            for i, repo in enumerate(repos):
                logger.info(f"Progress: {i+1}/{len(repos)}")
                repo_data = await self.collect_repo_data(session, repo)
                if repo_data:
                    results.append(repo_data)
                
                # Save checkpoint every 10 repos
                if (i + 1) % 10 == 0:
                    checkpoint_file = f"temp/datasets/checkpoint_{i+1}.json"
                    Path(checkpoint_file).write_text(json.dumps(results, indent=2))
                    logger.info(f"Saved checkpoint: {checkpoint_file}")
            
            return results

@logger.catch(reraise=True)
def main():
    # Initialize collector (no token = 60 requests/hour, with token = 5000 requests/hour)
    # For this demo, we'll collect a smaller sample
    collector = GitHubDataCollector(token=None)
    
    # Collect data for 50 repositories (manageable without token)
    logger.info("Starting GitHub data collection...")
    results = asyncio.run(collector.collect_data(max_repos=50))
    
    # Save final results
    output_file = Path("temp/datasets/github_repo_data_full.json")
    output_file.write_text(json.dumps(results, indent=2))
    logger.info(f"Saved {len(results)} repositories to {output_file}")
    
    # Create mini version (3 repos)
    mini_file = Path("temp/datasets/github_repo_data_mini.json")
    mini_file.write_text(json.dumps(results[:3], indent=2))
    
    # Create preview version
    preview = []
    for repo in results[:3]:
        preview_repo = repo.copy()
        # Truncate long fields
        if "commits" in preview_repo:
            for commit in preview_repo["commits"]:
                if "message" in commit and len(commit["message"]) > 200:
                    commit["message"] = commit["message"][:200] + "..."
        preview.append(preview_repo)
    
    preview_file = Path("temp/datasets/github_repo_data_preview.json")
    preview_file.write_text(json.dumps(preview, indent=2))
    
    logger.info("Data collection complete!")

if __name__ == "__main__":
    main()
