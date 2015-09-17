import os
dir = []
down = dir.append

def checkdir(directory):
    for file in os.listdir('/'.join(dir)):
        if not os.path.isfile(file):
            down(file)
            checkdir(directory)
        else:
            print(file)
