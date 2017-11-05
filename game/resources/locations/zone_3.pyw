import os, platform
from sys import argv
import json
sys.path.insert(0,"./game/resources/")
import core

with open("./game/resources/data.json", "r+") as gameState:
    gameState["currentZone"] = "zone 3"
    gameState["flag"]["newZone"] = True

    core.run()
