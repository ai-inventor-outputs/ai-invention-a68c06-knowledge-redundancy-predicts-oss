#!/bin/bash
echo "=== CGROUP ==="
if [ -f /sys/fs/cgroup/cpu.max ]; then
    echo "Type: cgroup v2"
    cat /sys/fs/cgroup/cpu.max
    cat /sys/fs/cgroup/memory.max 2>/dev/null || echo "memory.max: max"
    cat /sys/fs/cgroup/memory.current 2>/dev/null || echo "memory.current: N/A"
elif [ -f /sys/fs/cgroup/cpu/cpu.cfs_quota_us ]; then
    echo "Type: cgroup v1"
    cat /sys/fs/cgroup/cpu/cpu.cfs_quota_us
    cat /sys/fs/cgroup/cpu/cpu.cfs_period_us
    cat /sys/fs/cgroup/memory/memory.limit_in_bytes 2>/dev/null || echo "memory.limit: N/A"
    cat /sys/fs/cgroup/memory/memory.usage_in_bytes 2>/dev/null || echo "memory.usage: N/A"
else
    echo "Type: no cgroup"
fi
echo "=== GPU ==="
nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv,noheader 2>/dev/null || echo "No GPU"
