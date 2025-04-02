#!/usr/bin/env python3
"""
Image Optimizer for ZenDawn Travel Blog

This script automatically compresses and optimizes images from the source directories
and saves them to the website's images directory with appropriate naming and organization.

Usage:
    python optimize_images.py [--quality QUALITY] [--width WIDTH] [--watch]

Options:
    --quality QUALITY    JPEG quality (1-100), default is 85
    --width WIDTH        Maximum width in pixels, default is 1200
    --watch              Watch for new images and process them automatically
"""

import os
import sys
import time
import argparse
import shutil
from pathlib import Path
from PIL import Image, ImageOps

# Default settings
DEFAULT_QUALITY = 85
DEFAULT_MAX_WIDTH = 1200
SOURCE_DIR = 'src/destinations-india'
TARGET_DIR = 'src/images'

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Optimize images for web use')
    parser.add_argument('--quality', type=int, default=DEFAULT_QUALITY, 
                        help=f'JPEG quality (1-100), default is {DEFAULT_QUALITY}')
    parser.add_argument('--width', type=int, default=DEFAULT_MAX_WIDTH,
                        help=f'Maximum width in pixels, default is {DEFAULT_MAX_WIDTH}')
    parser.add_argument('--watch', action='store_true',
                        help='Watch for new images and process them automatically')
    return parser.parse_args()

def get_destination_path(source_path, width):
    """Determine the destination path for an optimized image."""
    # Extract the location name from the path (e.g., 'bhimbhetka' from 'src/destinations-india/bhimbhetka/images/file.jpg')
    parts = source_path.parts
    location_index = parts.index('destinations-india') + 1
    
    if location_index < len(parts):
        location = parts[location_index]
        
        # Create target directory if it doesn't exist
        target_dir = Path(TARGET_DIR) / location
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Determine output filename
        filename = source_path.stem
        
        # Use .jpg for photos to reduce file size
        if source_path.suffix.lower() in ['.png', '.jpeg', '.jpg']:
            # Use original extension for transparent images (detect in optimize_image)
            extension = '.jpg'
        else:
            # Keep original extension for other file types
            extension = source_path.suffix
            
        return target_dir / f"{filename}{extension}"
    
    # Fallback for unexpected path structure
    return Path(TARGET_DIR) / source_path.name

def has_transparency(img):
    """Check if the image has transparency (alpha channel or transparent pixels in PNG)."""
    if img.mode == 'RGBA':
        # Check if any pixel has alpha < 255
        extrema = img.getextrema()
        if len(extrema) == 4:  # RGBA
            if extrema[3][0] < 255:  # Min alpha < 255
                return True
    return False

def optimize_image(source_path, dest_path, max_width, quality):
    """Optimize a single image."""
    try:
        # Open and process the image
        with Image.open(source_path) as img:
            # Check if image needs to be resized
            if img.width > max_width:
                # Calculate new height to maintain aspect ratio
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.LANCZOS)
            
            # Auto-orient based on EXIF data
            img = ImageOps.exif_transpose(img)
            
            # Check transparency
            transparent = has_transparency(img)
            
            # Determine final output path and format
            if transparent:
                # Keep PNG for transparent images
                final_path = dest_path.with_suffix('.png')
                img.save(final_path, 'PNG', optimize=True)
            else:
                # Convert to JPEG for non-transparent images
                final_path = dest_path.with_suffix('.jpg')
                # Convert to RGB if needed
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                img.save(final_path, 'JPEG', quality=quality, optimize=True)
            
            # Get file sizes
            original_size = os.path.getsize(source_path)
            optimized_size = os.path.getsize(final_path)
            reduction = (1 - (optimized_size / original_size)) * 100
            
            print(f"Optimized: {source_path.name}")
            print(f"  Original: {original_size / 1024:.1f} KB")
            print(f"  Optimized: {optimized_size / 1024:.1f} KB")
            print(f"  Reduction: {reduction:.1f}%")
            print(f"  Saved to: {final_path}")
            
            return final_path
            
    except Exception as e:
        print(f"Error optimizing {source_path.name}: {e}")
        return None

def scan_and_optimize(max_width, quality):
    """Scan for images and optimize them."""
    source_dir = Path(SOURCE_DIR)
    processed_count = 0
    
    # Find all image files in source directories
    for location_dir in source_dir.iterdir():
        if not location_dir.is_dir():
            continue
            
        images_dir = location_dir / 'images'
        if not images_dir.exists() or not images_dir.is_dir():
            continue
            
        # Process each image in the images directory
        for image_path in images_dir.glob('*'):
            if not image_path.is_file():
                continue
                
            # Check if it's an image file
            if image_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                dest_path = get_destination_path(image_path, max_width)
                
                # Skip if destination file already exists and is newer
                if dest_path.exists() and os.path.getmtime(dest_path) >= os.path.getmtime(image_path):
                    print(f"Skipping {image_path.name} (already optimized)")
                    continue
                    
                # Optimize the image
                if optimize_image(image_path, dest_path, max_width, quality):
                    processed_count += 1
    
    return processed_count

def watch_for_changes(max_width, quality):
    """Watch for new or modified images and optimize them."""
    print("Watching for image changes. Press Ctrl+C to stop.")
    
    try:
        last_scan_time = time.time()
        
        while True:
            # Perform initial scan
            processed = scan_and_optimize(max_width, quality)
            if processed > 0:
                print(f"Processed {processed} images.")
            
            # Sleep for a while before next scan
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nWatcher stopped.")

def main():
    """Main function."""
    args = parse_args()
    
    # Ensure quality is within valid range
    quality = max(1, min(100, args.quality))
    
    # Create target directory if it doesn't exist
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    if args.watch:
        watch_for_changes(args.width, quality)
    else:
        processed = scan_and_optimize(args.width, quality)
        print(f"Processed {processed} images.")
        
if __name__ == "__main__":
    main() 