import sys,os,subprocess,string
from platform import python_version
from html.parser import HTMLParser


if '2.' == python_version()[:1]:
    print("This program requires Python 3 in order to properly function.\nA backwards compatible version may be available in the future.")
    input("End of line.")
    sys.exit()
else:
    from urllib.request import urlopen

try:
    from bs4 import BeautifulSoup
except:
    answer = input("Your system does not have BeautifulSoup installed. Do you want to install it?")
    if 'y' or 'Y' in answer:
        os.system('python -m pip install --upgrade beautifulsoup4')
    else:
        print("Without BeautifulSoup, this process will not function.")
        input("End of line.")

def say(mess):
    try:
        mess = str(mess)
        try:
            os.remove("Speak.txt")
        except:
            pass
        #Create the Visual Basic code which will speak the text
        file = open("Speak.txt",'w')
        file.write("""speaks="{}"\nDim speaks, speech\nSet speech=CreateObject("sapi.spvoice")\nspeech.Speak speaks""".format(mess))
        file.close()
        
        try:
            os.remove("Speak.vbs")
        except:
            base_file, ext = os.path.splitext("Speak.txt")
            os.rename("Speak.txt", base_file + ".vbs")
        #Turn the .txt into a Visual Basic file to be executed
        base_file, ext = os.path.splitext("Speak.txt")
        os.rename("Speak.txt", base_file + ".vbs")
        #Execute the file
        subprocess.call(['cscript.exe', "Speak.vbs"])
    except:
        print("Startup failed. Please rerun the program.")

say("Starting up...")

#The following is not my code -Z

#Filters nonprintable characters from a string
def filter_nonprintable(text):
    # Get the difference of all ASCII characters from the set of printable characters
    nonprintable = set([chr(i) for i in range(128)]).difference(string.printable)
    # Use translate to remove all non-printable characters
    return text.translate({ord(character):None for character in nonprintable})


#Credit where credit is due Eloff

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

#End of that which isn't my code -Z

def parse_it(text,mode='speak'): #Modes are read, for being read by user, and speak, for being spoken by a program
    #Removes all unicode characters, nonprintable characters, and HTML code
    text = bytes(strip_tags(filter_nonprintable(text)),'utf-8').decode('unicode_escape').encode('ascii','ignore')
    if mode=='speak':
        #Removes newline and return characters
        return str(text.decode('utf-8')).replace('\n','').replace('\r',' ').replace('"',"'").replace('.','. ')
    elif mode=='read':
        #Returns the text as it is without the unicode and HTML characters
        return str(text.decode('utf-8'))


def get_story(url,search='storytext'):
    #Opens and parses the URL with BeautifulSoup
    soup = BeautifulSoup(urlopen(str(url)))
    #Finds the path and contents given by the search
    text = str(soup.find(class_=search))
    return text

def easy_read(text):
    text = text.replace(':', ': ').replace('!','! ').replace('?','? ').replace('. . .','...').replace('é','e').replace('1','1 ').replace('2','2 ').replace('3','3 ').replace('4','4 ').replace('5','5 ').replace('6','6 ').replace('7','7 ').replace('8','8 ').replace('9','9 ').replace('0','0 ').replace('!  ','! ').replace('?  ','? ').replace(':  ',': ').replace(';','; ').replace(';  ','; ')

say("Please input your URL.")
text = parse_it(get_story(input("Please enter the URL of the Fanfiction.net story: ")))
print(text)
say(text)
input("End of line.")
