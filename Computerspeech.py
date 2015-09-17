
def say(mess):
    print(mess)
    try:
        mess = str(mess)
        try:
            os.remove("Speak.txt")
        except:
            pass
        # Create the Visual Basic code which will speak the text
        file = open("Speak.txt", 'w')
        file.write(
            """speaks="{}"\nDim speaks, speech\nSet speech=CreateObject("sapi.spvoice")\nspeech.Speak speaks"""
                .format(mess))
        file.close()
        
        try:
            os.remove("Speak.vbs")
        except:
            base_file, ext = os.path.splitext("Speak.txt")
            os.rename("Speak.txt", base_file + ".vbs")
        # Turn the .txt into a Visual Basic file to be executed
        base_file, ext = os.path.splitext("Speak.txt")
        os.rename("Speak.txt", base_file + ".vbs")
        # Execute the file
        call(['cscript.exe', "Speak.vbs"])
    except:
        print("Vocalization failed.")

say("Initializing...")
while 1:
    say(input("Please input the message: ").replace('"', ' ').replace("'", ' '))

