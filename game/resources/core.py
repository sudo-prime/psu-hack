import json
import os, sys
import platform
import subprocess
from shutil import copyfile

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

        # Name entry

        if gameState["flag"]["nameConfirm"] == True:
            path = "./name.txt"
            writeFile = open(path, "w")
            writeFile.close()

            nameFile = open(path, "r")

            copyfile("./game/resources/done.pyw", "done.pyw")

        # Write result to game.txt
        with open("./game.txt", "r+") as game:
            game.truncate()
            game.write("")
            game.close()

if __name__ == "__main__":
    run()
