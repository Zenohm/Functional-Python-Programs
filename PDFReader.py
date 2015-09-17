import PyPDF2
import os
import urllib.request

from subprocess import call


def say(mess):
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

path = "C:/Users/Isaac/Documents/Mass_Effect_-_Ascension.pdf"

def parse_it(text):
    #Removes all unicode characters, nonprintable characters, and HTML code
    text = str(bytes(text,'utf-8').decode('unicode_escape').encode('ascii','ignore').decode('utf-8'))
    #Removes newline and return characters
    return text.replace('\r',' ').replace('"',"'").replace('.','. ')

def getText(path,page):
    return parse_it(PyPDF2.PdfFileReader(path).getPage(page).extractText().replace('\u2122',"'"))

say("Initializing...")
path = input("Please enter the path of a PDF: ")
if 'http://' in path or 'https://' in path:
    path = urllib.request.urlopen(path)
    file = open('PDF2BEREAD.pdf','wb')
    file.write(path.read())
    file.close()
    path = 'C:/Users/Isaac/PDF2BEREAD.pdf'
first_page = int(input("Please enter the beginning page: ")) - 1
for each_page in range(first_page,PyPDF2.PdfFileReader(path).getNumPages()):
    text = getText(path,each_page)
    print('\r \r \r \r' + str(each_page + 1))
    print(text)
    text = text.replace("\'", '').replace('\"', '').replace('\n', ' ').replace('Tali','Tahlie').replace('tali','tahlie').replace ('Yalo',' Yah-lo ').replace('Noveria',' No-veir-eaah ').replace('Binary','Bi-nary')
    say(text)
input("End of line.")
