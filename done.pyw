import os, platform
from sys import argv
import json

with open("name.txt", "r") as nameFile:
    name = nameFile.readline()
    if name == "":
        writeFile = open("invalid.txt", "w")
        writeFile.write("Please enter a name.")
        writeFile.close()
    elif name.isspace():
        writeFile = open("invalid.txt", "w")
        writeFile.write("Don't just enter whitespace, dick.")
        writeFile.close()
    else:
        with open("./game/resources/data.json", "r+") as data:
            gameState = json.load(data)
            name = name.rstrip()
            gameState["character"]["name"] = name
            gameState["flag"]["nameConfirm"] = False

            nameFile.close()

            data.seek(0)
            json.dump(gameState, data, indent=4)
            data.truncate()

            if platform.system() == "Windows":
                os.system("taskkill /f /im notepad.exe")
            else:
                os.system("pkill -9 \"TextEdit\"")

            if os.path.exists("invalid.txt"):
                os.remove("invalid.txt")

            os.remove("name.txt")
            os.remove(argv[0])
