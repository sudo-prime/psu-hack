import json
import os, sys
import platform
import subprocess
from shutil import copyfile
from shutil import rmtree

if platform.system() == "Windows":
    namePath = ".\\..\\..\\name.txt"
    gamePath = ".\\..\\..\\game.txt"
    fromDonePath = "done.pyw"
    toDonePath= ".\\..\\..\\done.pyw"
    dataPath = "data.json"
    nearbyPath = ".\\..\\..\\nearby"
else:
    namePath = "./name.txt"
    gamePath = "./game.txt"
    fromDonePath = "./game/resources/done.pyw"
    toDonePath= "done.pyw"
    dataPath = "./game/resources/data.json"
    nearbyPath = "./nearby"

def getFromPath(fileName, fileType):
    if platform.system() == "Windows":
        if fileType == "location":
            return ".\\locations\\" + fileName
    else:
        if fileType == "location":
            return "./game/resources/locations/" + fileName

def getToPath(fileName, fileType):
    if platform.system() == "Windows":
        if fileType == "location":
            return ".\\..\\..\\nearby\\" + fileName
    else:
        if fileType == "location":
            return "./nearby/" + fileName

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
    with open(formatPath(dataPath)) as data:
        gameState = json.load(data)

        # Name entry
        if gameState["flag"]["confirmName"] == True:
            path = namePath
            writeFile = open(path, "w")
            writeFile.close()

            copyfile(fromDonePath, toDonePath)
        # Update zone information
        if (gameState["flag"]["newZone"] == True):
            # If the nearby folder exists
            if os.path.exists(nearbyPath):
                rmtree(nearbyPath)

            os.mkdir(nearbyPath)

            for location in gameState["nearby"][gameState["currentZone"]]:
                print location

            if gameState["currentZone"] in gameState["flag"]["specialZones"]:
                gameState["gameText"] = gameState["zoneText"][gameState["currentZone"]]["specialZones"]
                gameState["flag"]["newZone"] == False
            elif gameState["currentZone"] in gameState["flag"]["visitedZones"]:
                gameState["gameText"] = gameState["zoneText"][gameState["currentZone"]]["visitedZones"]
                gameState["flag"]["newZone"] == False
            else:
                gameState["gameText"] = gameState["zoneText"][gameState["currentZone"]]["new"]
                gameState["flag"]["newZone"] == False
                gameState["flag"]["visitedZones"].append(gameState["currentZone"])

        #print "current zone: " + gameState["currentZone"]
        #print "visited zones: " + str(gameState["flag"]["visitedZones"])

        # Write result to game.txt
        gameFile = open(gamePath, "w")
        gameFile.write(gameState["gameText"])
        gameFile.close()

if __name__ == "__main__":
    run()
