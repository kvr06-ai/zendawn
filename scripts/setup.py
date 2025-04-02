#!/usr/bin/env python3
"""
Setup script for the ZenDawn image optimizer

This script creates a virtual environment and installs required Python packages.
"""

import os
import sys
import subprocess
from pathlib import Path

# Virtual environment location
VENV_DIR = Path(__file__).parent / 'venv'

def check_python():
    """Check Python version."""
    if sys.version_info < (3, 6):
        print("Error: Python 3.6 or higher is required.")
        return False
    return True

def create_venv():
    """Create a virtual environment."""
    if VENV_DIR.exists():
        print(f"Virtual environment already exists at {VENV_DIR}")
        return True
        
    print(f"Creating virtual environment at {VENV_DIR}...")
    try:
        subprocess.check_call([sys.executable, '-m', 'venv', str(VENV_DIR)])
        print("Virtual environment created successfully!")
        return True
    except Exception as e:
        print(f"Error creating virtual environment: {e}")
        return False

def get_venv_python():
    """Get the path to the Python executable in the virtual environment."""
    if os.name == 'nt':  # Windows
        return VENV_DIR / 'Scripts' / 'python.exe'
    else:  # Unix/Linux/MacOS
        return VENV_DIR / 'bin' / 'python'

def install_requirements():
    """Install required packages in the virtual environment."""
    requirements = ['pillow']
    venv_python = get_venv_python()
    
    if not venv_python.exists():
        print(f"Error: Virtual environment Python not found at {venv_python}")
        return False
    
    print("Installing required packages in the virtual environment...")
    try:
        for package in requirements:
            print(f"Installing {package}...")
            subprocess.check_call([
                str(venv_python), '-m', 'pip', 'install', package
            ])
        print("All packages installed successfully!")
        return True
    except Exception as e:
        print(f"Error installing packages: {e}")
        return False

def create_runner_script():
    """Create a shell script to run the optimizer with the virtual environment."""
    scripts_dir = Path(__file__).parent
    
    # Create bash script for Unix/Linux/MacOS
    if os.name != 'nt':
        runner_path = scripts_dir / 'optimize.sh'
        with open(runner_path, 'w') as f:
            f.write(f"""#!/bin/bash
# Automatically run the image optimizer using the virtual environment

SCRIPT_DIR="$( cd "$( dirname "${{BASH_SOURCE[0]}}" )" && pwd )"
VENV_PYTHON="$SCRIPT_DIR/venv/bin/python"
OPTIMIZER="$SCRIPT_DIR/optimize_images.py"

# Activate virtual environment and run optimizer
"$VENV_PYTHON" "$OPTIMIZER" "$@"
""")
        # Make the script executable
        os.chmod(runner_path, 0o755)
        print(f"Created runner script: {runner_path}")
    
    # Create batch script for Windows
    else:
        runner_path = scripts_dir / 'optimize.bat'
        with open(runner_path, 'w') as f:
            f.write(f"""@echo off
:: Automatically run the image optimizer using the virtual environment

set SCRIPT_DIR=%~dp0
set VENV_PYTHON=%SCRIPT_DIR%venv\\Scripts\\python.exe
set OPTIMIZER=%SCRIPT_DIR%optimize_images.py

:: Run optimizer
"%VENV_PYTHON%" "%OPTIMIZER%" %*
""")
        print(f"Created runner script: {runner_path}")
    
    return True

def create_readme():
    """Create a README file with usage instructions."""
    readme_path = Path(__file__).parent / "README.md"
    
    if readme_path.exists():
        return
        
    with open(readme_path, 'w') as f:
        f.write("""# ZenDawn Image Optimizer

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
scripts\\optimize.bat
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
""")

def main():
    """Main function."""
    print("Setting up ZenDawn Image Optimizer...")
    
    if not check_python():
        return False
        
    if not create_venv():
        return False
        
    if not install_requirements():
        return False
        
    if not create_runner_script():
        return False
        
    create_readme()
    
    print("\nSetup complete! You can now use the image optimizer:")
    
    if os.name != 'nt':  # Unix/Linux/MacOS
        print("  ./scripts/optimize.sh")
        print("  ./scripts/optimize.sh --watch")
    else:  # Windows
        print("  scripts\\optimize.bat")
        print("  scripts\\optimize.bat --watch")
        
    return True

if __name__ == "__main__":
    sys.exit(0 if main() else 1) 