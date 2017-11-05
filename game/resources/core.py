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

<<<<<<< HEAD
def run():
    with open("data.json") as data:
        gameState = json.load(data)
        print gameState["name"]
=======
with open("data.json") as data:
    gameState = json.load(data)
    print gameState["name"]

def run():
>>>>>>> b03707551a74d87210386bc27151016fcc012e5c
