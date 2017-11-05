import json
import os
import platform
import subprocess

def open_file(path):
    if platform.system() == "Windows":
        subprocess.Popen('explorer "{0}"'.format(path))
    elif platform.system() == "Darwin":
        os.system('open "%s"' % "actions")
    else:
        subprocess.Popen(["xdg-open", path])

with open("data.json") as data:
    gameState = json.load(data)
    print gameState["name"]

def run():
