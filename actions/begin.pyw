import subprocess
import game.resources.core

with open("data.json") as data:
    gameState = json.load(data)

    gameState.flag["gameStarted"] = "true"
