#Filters nonprintable characters from a string
def filter_nonprintable(text):
    import string
    # Get the difference of all ASCII characters from the set of printable characters
    nonprintable = set([chr(i) for i in range(128)]).difference(string.printable)
    # Use translate to remove all non-printable characters
    return text.translate({ord(character):None for character in nonprintable})

#SLOW AND NOT VERY USEFUL EXCEPT ON SMALL SCALE
def remove_html(string):
    string = list(string)
    while '<' in string:
        del string[string.index('<'):string.index('>')]
    return ''.join(string)


#Credit where credit is due Eloff
from html.parser import HTMLParser

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
#Credit ends
#This is awesome ^
#For Fanfiction.net

#Zen Code
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
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    #Opens and parses the URL with BeautifulSoup
    soup = BeautifulSoup(urlopen(str(url)))
    #Finds the path and contents given by the search
    text = str(soup.find(class_=search))
    return text

def easy_read(text):
    text = text.replace(':', ': ').replace('!','! ').replace('?','? ').replace('. . .','...').replace('é','e').replace('1','1 ').replace('2','2 ').replace('3','3 ').replace('4','4 ').replace('5','5 ').replace('6','6 ').replace('7','7 ').replace('8','8 ').replace('9','9 ').replace('0','0 ').replace('!  ','! ').replace('?  ','? ').replace(':  ',': ').replace(';','; ').replace(';  ','; ')

def get_it(module, modulesub,install=''):
    if not install:
        install = module
    if not modulesub:
        try:
            exec("import {}".format(str(module)))
        except:
            answer = input("Your system does not have {} installed. Do you want to install it?".format(module))
            if 'y' or 'Y' in answer:
                os.system('python -m pip install --upgrade {}'.format(install))
            else:
                print("Without {}, this process will not function.".format(module))
                input("End of line.")
    else:
        try:
            exec("from {0} import {1}".format(str(module),str(modulesub)))
        except:
            answer = input("Your system does not have {} installed. Do you want to install it?".format(module))
            if 'y' or 'Y' in answer:
                os.system('python -m pip install --upgrade {}'.format(install))
            else:
                print("Without {}, this process will not function.".format(module))
                input("End of line.")

def check_version(version):
    from platform import python_version
    if version == python_version()[:len(version)-1]:
        print("This program requires Python {} in order to properly function.\nA backwards compatible version may be available in the future.".format(str(version)))
        input("End of line.")
        sys.exit()
    else:
        from urllib.request import urlopen
