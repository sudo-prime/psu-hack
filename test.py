import os
import platform
import subprocess

def open_file(path):
    if platform.system() == "Windows":
        subprocess.Popen(r'explorer,' + path)
    elif platform.system() == "Darwin":
        os.system('open "%s"' % "actions")
    else:
        subprocess.Popen(["xdg-open", path])

open_file(".\\actions\\attack")
