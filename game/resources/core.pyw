import json
import os, sys
import platform
import subprocess
from shutil import copyfile

if platform.system() == "Windows":
    namePath = ".\\..\\..\\name.txt"
    gamePath = ".\\..\\..\\game.txt"
    fromDonePath = "done.pyw"
    toDonePath= ".\\..\\..\\done.pyw"
    dataPath = "data.json"
else:
    namePath = "./name.txt"
    gamePath = "./game.txt"
    fromDonePath = "./game/resources/done.pyw"
    toDonePath= "done.pyw"
    dataPath = "./game/resources/data.json"

def open_file(path):
    if platform.system() == "Windows":
        path = path.replace("/", "\\")
        subprocess.Popen('explorer "{0}"'.format(path))
    elif platform.system() == "Darwin":
        path = path.replace("\\", "/")
        os.system('open "%s"' % "actions")
    else:
        subprocess.Popen(["xdg-open", path])

def formatPath(path):
    if platform.system() == "Windows":
        path = path.replace("/", "\\")
        return path
    elif platform.system() == "Darwin":
        path = path.replace("\\", "/")
        return path
    else:
        return "INVALID_PATH"

def run():
    with open(formatPath("./game/resources/data.json")) as data:
        gameState = json.load(data)

        # Name entry

        if gameState["flag"]["nameConfirm"] == True:
            path = "./name.txt"
            writeFile = open(path, "w")
            writeFile.close()

            copyfile("./game/resources/done.pyw", "done.pyw")

        # Write result to game.txt
        with open("./game.txt", "r+") as game:
            game.truncate()
            game.write("")
            game.close()

if __name__ == "__main__":
    run()
