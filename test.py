import subprocess
import sys


if sys.platform == "win32":
    subprocess.Popen(r'explorer /select,".\actions\attack"')

elif sys.platform == "darwin"
    #do some shit
