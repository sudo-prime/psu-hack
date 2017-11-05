import json
import os
import platform
import subprocess

def open_file(path):
    if platform.system() == "Windows":
        subprocess.Popen('explorer "{0}"'.format(path))
    elif platform.system() == "Darwin":
        os.system('open "%s"' % path)
    else:
        subprocess.Popen(["xdg-open", path])

def run():
    with open("./game/resources/data.json") as data:
        gameState = json.load(data)

        with open("../../game.txt", "r+") as game:
            game.truncate()
            game.write(gameState["flag"]["gameStarted"])
            game.close()

#open_file("./game.txt") WORKS MAC
