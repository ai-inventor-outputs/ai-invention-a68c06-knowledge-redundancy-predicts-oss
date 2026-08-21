#!/usr/bin/env python
"""Convert PDF pages to PNG images for visual review."""
import fitz  # pymupdf
import os

pdf_path = "paper.pdf"
output_dir = "page_images"

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Open PDF
doc = fitz.open(pdf_path)

# Convert each page to PNG at 150 DPI
for page_num in range(len(doc)):
    page = doc[page_num]
    # 150 DPI zoom factor
    zoom = 150 / 72
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    output_path = os.path.join(output_dir, f"page_{page_num + 1:02d}.png")
    pix.save(output_path)
    print(f"Saved {output_path}")

print(f"\nConverted {len(doc)} pages to PNG images at 150 DPI")
