import subprocess
import core

with open("data.json") as data:
    gameState = json.load(data)

    gameState.flag["gameStarted"] = "true"
