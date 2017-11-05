import json
import os
import platform
import subprocess

def open_file(path):
    if platform.system() == "Windows":
        path = path.replace("/", "\\")
        subprocess.Popen('explorer "{0}"'.format(path))
    elif platform.system() == "Darwin":
        path = path.replace("\\", "/")
        os.system('open "%s"' % "actions")
    else:
        subprocess.Popen(["xdg-open", path])

def run():
    with open("data.json") as data:
        gameState = json.load(data)
        print gameState["name"]

open_file("./game.txt")
