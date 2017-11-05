import subprocess
import sys
import json
sys.path.insert(0,"./game/resources/")
import core

with open("./game/resources/data.json", "r+") as data:
    gameState = json.load(data)

    gameState["flag"]["gameStarted"] = True

    data.truncate()
    data.write(json.dumps(gameState))

    core.run()
