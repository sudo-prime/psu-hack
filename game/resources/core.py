import json

with open("data.json") as data:
    gameState = json.load(data)
    print gameState["name"]
