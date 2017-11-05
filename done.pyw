import os, platform
import sys
import json
sys.path.insert(0,"./game/resources/")
import core

with open("name.txt", "r") as nameFile:
    name = nameFile.readline()
    if name == "":
        writeFile = open("invalid.txt", "w")
        writeFile.write("Please enter a name.")
        writeFile.close()
        nameFile.close()
    elif name.isspace():
        writeFile = open("invalid.txt", "w")
        writeFile.write("Don't just enter whitespace, dick.")
        writeFile.close()
        nameFile.close()
    else:
        with open("./game/resources/data.json", "r+") as data:
            gameState = json.load(data)
            name = name.rstrip()
            gameState["character"]["name"] = name
            gameState["flag"]["nameConfirm"] = False
            gameState["currentZone"] = "start"
            gameState["flag"]["newZone"] = True

            nameFile.close()

            data.seek(0)
            json.dump(gameState, data, indent=4)
            data.truncate()

            writeFile = open("invalid.txt", "w")
            writeFile.write("Don't just enter whitespace, dick.")
            writeFile.close()

            if platform.system() == "Windows":
                os.system("taskkill /f /im notepad.exe")
            else:
                os.system("pkill -9 \"TextEdit\"")

            if os.path.exists("invalid.txt"):
                os.remove("invalid.txt")

            os.remove("name.txt")
            core.run()
            os.remove(argv[0])
