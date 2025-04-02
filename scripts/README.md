# ZenDawn Image Optimizer

A tool to automatically optimize images for the ZenDawn travel blog website.

## Setup

Run the setup script once to create a virtual environment and install dependencies:

```
python scripts/setup.py
```

## Usage

After setup, optimize all images using:

```
# On macOS/Linux
./scripts/optimize.sh

# On Windows
scripts\optimize.bat
```

Watch for image changes (continuously monitors and optimizes):

```
./scripts/optimize.sh --watch
```

Customize quality and width:

```
./scripts/optimize.sh --quality 80 --width 1500
```

## Options

- `--quality QUALITY`: JPEG quality (1-100), default is 85
- `--width WIDTH`: Maximum width in pixels, default is 1200
- `--watch`: Watch for new images and process them automatically

## How It Works

1. The script scans the `src/destinations-india/*/images/` directories for image files
2. It optimizes each image (resizes, compresses) and saves it to `src/images/{location}/`
3. Images with transparency are saved as PNG, others as JPEG for better compression
4. Optimized images are tracked by modification time to avoid reprocessing

## Dependencies

- Python 3.6+
- Pillow (PIL Fork) - installed automatically in the virtual environment
