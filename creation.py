import json
import sys
sys.path.insert(0,"./game/resources/")
import core
import os
import platform

def run():
    with open("character.json", "r+") as data:
        gameState = json.load(data)
        gameState["appearence"]["age"] = "12345678"
        data.seek(0)        # <--- should reset file position to the beginning.
        json.dump(gameState, data, indent=4)
        data.truncate()

def create():
    with open("./game/resources/data.json", "r+") as data:
        gameState = json.load(data)

        path = "./name.txt"
        writeFile = open(path, "w")
        writeFile.close()

        readFile = open(path, "r")

        core.open_file(path)

        reading = True

        while reading:
            name = readFile.readline()
            if name != "":
                reading = False

        readFile.close()

        if platform.system() == "Windows":
            os.system("taskkill /f /im notepad.exe")
        else:
            os.system("pkill -9 \"TextEdit\"")

        os.remove(path)


        gameState["character"]["name"] = name


        data.seek(0)        # <--- should reset file position to the beginning.
        json.dump(gameState, data, indent=4)
        data.truncate()

create()
