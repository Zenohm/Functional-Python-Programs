import os

def volume_up(value=10000):
    os.system("nircmd.exe changesysvolume %d" %value)

def volume_down(value=10000):
    os.system("nircmd.exe changesysvolume -%d" %value)

def volume_set(value=15000):
    os.system("nircmd.exe setsysvolume %d" %value)

def mute(state=2):
    os.system("nircmd.exe mutesysvolume %d" %state)

def speak(text,clip=0):
    if clip:
        text = "~$clipboard$"
    os.system("nircmd.exe speak text %s" %text)

def screen_off():
    os.system("nircmd.exe monitor off")

def screen_on():
    os.system("nircmd.exe monitor on")

def standby():
    os.system("nircmd.exe standby")

def logoff():
    os.system("nircmd.exe exitwin logoff")

def reboot():
    os.system("nircmd.exe exitwin reboot")

def shutdown():
    os.system("nircmd.exe exitwin poweroff")

def Qbox(question,title="Question",action=""):
    os.system("nircmd.exe qboxcom "+'"'+str(question)+'"'+'"'+title+'"'+action)

def nir(inp):
    os.system("nircmd.exe %s" %inp)
