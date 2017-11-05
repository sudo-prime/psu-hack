import os
import shutil
import subprocess
import sys
sys.path.insert(0,"./game/resources/")
import core

if os.path.exists('action'):
    shutil.rmtree("action")


os.mkdir("action")

file = open("./action/test.txt", "w")

file.write("sah")

file.close()

path = ".\\action\\test.txt"
core.open_file(path)
