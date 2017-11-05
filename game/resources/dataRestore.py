import os
from shutil import copyfile

if os.path.exists('data.json'):
    os.remove("data.json")
copyfile("./spare.json", "data.json")
