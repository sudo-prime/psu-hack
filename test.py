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
