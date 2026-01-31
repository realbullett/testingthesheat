#!/usr/bin/env python3
"""
Setup script for NotePad Pro
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        subprocess.run(cmd, check=True, shell=True)
        print(f"✓ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        return False


def main():
    """Main setup function"""
    print("=" * 60)
    print("NotePad Pro - Setup")
    print("=" * 60)
    
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("✗ Python 3.8 or higher is required!")
        print(f"  Current version: {sys.version}")
        sys.exit(1)
    
    print(f"✓ Python version: {sys.version.split()[0]}")
    
    # Create virtual environment
    venv_path = project_dir / "venv"
    
    if venv_path.exists():
        print("\n✓ Virtual environment already exists")
    else:
        if not run_command(
            f"{sys.executable} -m venv venv",
            "Creating virtual environment"
        ):
            sys.exit(1)
    
    # Determine pip path
    if sys.platform == "win32":
        pip_path = venv_path / "Scripts" / "pip"
    else:
        pip_path = venv_path / "bin" / "pip"
    
    # Install dependencies
    if not run_command(
        f"{pip_path} install -r requirements.txt",
        "Installing dependencies"
    ):
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✓ Setup completed successfully!")
    print("=" * 60)
    print("\nTo run NotePad Pro:")
    print("  Linux/macOS: ./run.sh")
    print("  Windows:     run.bat")
    print("  Or directly: python main.py (after activating venv)")
    print("\n")


if __name__ == "__main__":
    main()
