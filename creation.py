import json

def run():
    with open("character.json", "r+") as data:
        gameState = json.load(data)
        gameState["appearence"]["age"] = 20
        data.seek(0)        # <--- should reset file position to the beginning.
        json.dump(gameState, data, indent=4)
        data.truncate()

run()
