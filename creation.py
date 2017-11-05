import json

def run():
    with open("character.json", "r+") as data:
        gameState = json.load(data)
        gameState["appearence"]["age"] = "12345678"
        data.seek(0)        # <--- should reset file position to the beginning.
        json.dump(gameState, data, indent=4)
        data.truncate()

def create():
    with open("character.json", "r+") as data:
        gameState = json.load(data)

        gameState["appearence"]["name"] = raw_input('What is your name? ')


        data.seek(0)        # <--- should reset file position to the beginning.
        json.dump(gameState, data, indent=4)
        data.truncate()

create()
