import sys
from cx_Freeze import setup, Executable

# Dependencies and includes
build_exe_options = {
    "packages": ["tkinter", "PIL", "selenium", "time","random","string","os"],
    "includes": ["tkinter", "PIL.Image", "PIL.ImageTk"],
}

# Create the Executable
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executable = Executable(
    script="whatmsg.py",  # Replace with the name of your Python script
    base=base,
    icon="icon.ico",  # Replace with the path to your .ico icon file
)

# Setup
setup(
    name="WhatMsg",
    version="1.0",
    description="Your Application Description",
    options={"build_exe": build_exe_options, "bdist_msi": {"add_to_path": True}},
    executables=[executable],
)
