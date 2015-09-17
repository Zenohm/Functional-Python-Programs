import os
from time import sleep
for x in range(100):
    os.system("nircmd.exe monitor off")
    sleep(60)
    os.system("nircmd.exe monitor on")
    sleep(20)

