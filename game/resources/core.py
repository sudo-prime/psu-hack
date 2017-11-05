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
    with open("./game/resources/data.json") as data:
        gameState = json.load(data)

        with open("./game.txt", "r+") as game:
            game.truncate()
            game.write(str(gameState[""]["gameStarted"]))
            game.close()
