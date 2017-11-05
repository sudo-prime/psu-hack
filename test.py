"""import subprocess
import sys
import platform


if platform.system() == "Windows":
    subprocess.Popen(r'explorer /select,".\actions\attack"')

elif sys.platform == "darwin"
    #do some shit
"""
import os
import platform
import subprocess
def open_file(path):
    if platform.system() == "Windows":
        subprocess.Popen(r'explorer /select,' + path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

open_file(".\\actions\\attack")
