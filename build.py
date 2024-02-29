import subprocess
import shutil
import os

def build_and_cleanup():
    # Run pyinstaller command
    subprocess.run(["pyinstaller", ".\\main.py", "--onefile", "-w"])

    # Move main.exe from dist folder to current directory
    shutil.move(".\\dist\\main.exe", ".\\")

    # Remove build and dist folders
    shutil.rmtree(".\\build")
    shutil.rmtree(".\\dist")

if __name__ == "__main__":
    build_and_cleanup()