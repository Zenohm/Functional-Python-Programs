import os
import time
from subprocess import call
from platform import python_version
from os.path import expanduser
home = expanduser("~")


if '2.' == python_version()[:1]:
    print("This program requires Python 3 in order to properly function.\nA backwards compatible version may be available in the future.")
    input("End of line.")
    sys.exit()
else:
    try:
        from urllib.request import urlopen
    except:
        from urllib import urlopen

try:
    from gtts import gTTS
except:
    answer = input("Your system does not have Google's Text to Speech API installed. Do you want to install it?")
    if 'y' or 'Y' in answer:
        os.system('python -m pip install --upgrade gTTS')
    else:
        print("Without the Google Text to Speech API, this process will not sound natural.")

try:
    from bs4 import BeautifulSoup
except:
    answer = input("Your system does not have BeautifulSoup installed. Do you want to install it?")
    if 'y' or 'Y' in answer:
        os.system('python -m pip install --upgrade beautifulsoup4')
    else:
        print("Without BeautifulSoup, this process will not be able to pull text from websites successfully.")

try:
    import PyPDF2
except:
    answer = input("Your system does not have PyPDF2 installed. Do you want to install it?")
    if 'y' or 'Y' in answer:
        os.system('python -m pip install --upgrade PyPDF2')
    else:
        print("Without PyPDF2, this process will not be able to process PDF files successfully.")

try:
    def say(mess,title='Speak'):
            title += '.mp3'
            tts = gTTS(mess)
            tts.save(home+'\\'+title)
            os.system("start /MIN {}".format(home+'\\'+title))
except:
    def say(mess,title='Speak'):
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


def parse_it(text):
    #Removes all unicode characters, nonprintable characters, and HTML code
    text = str(bytes(text,'utf-8').decode('unicode_escape').encode('ascii','ignore').decode('utf-8'))
    #Removes newline and return characters
    return text.replace('\n','').replace('\r',' ').replace('"',"'").replace('.','. ')

def get_story_fanfiction(url, search='storytext'):
    # Opens and parses the URL with BeautifulSoup
    soup = BeautifulSoup(urlopen(str(url)))
    # Finds the path and contents given by the search
    try:
        text = soup.find(class_=search).text
        return text
    except:
        print('End of line.')

def get_story_deviantart(url):
    soup = BeautifulSoup(urlopen(str(url)))
    text = parse_it(soup.select('#devskin > div > div > div.gr-body > div > div > div')[0].text)
    return text

def get_story_wattpad(url, search="panel panel-reading", mode='singular'):  # Modes are singular and plural
    #Opens and parses the URL with BeautifulSoup
    soup = BeautifulSoup(urlopen(str(url)))
    #Finds the path and contents given by the search
    if mode == 'singular':
        text = soup.find(class_="panel panel-reading")
    elif mode == 'plural':
        text = soup.find_all(class_="panel panel-reading")
    return text

def OmniReader(text):
    if 'wattpad' in text:
        try:
            res = soup.find_all('script')
            # Get rid of all those pesky spaces and new lines
            res[5].contents[0].replace('\n      ', '').replace(' ', '')
        except:
            pass

        url = text
        number_of_pages = input("How many pages are in the story: ")
        # Iterates through the pages of the story
        for each_page in range(int(number_of_pages) + 1):
            if each_page:
                #Designed to cope with Wattpad's fucking weird multi-page system
                text = get_story_wattpad(url + '/page/' + str(each_page), mode='plural')[1]
            else:
                #Meant for the first page because fuck Wattpad
                text = get_story_wattpad(url)
            #Get all the text in one big orgy array
            paragraphs = text.find_all('p')
            #Iterates through the paragraphs in each page of the story
            for each_paragraph in range(len(paragraphs)):
                #Get all the text segments
                paragraphs[each_paragraph] = paragraphs[each_paragraph].text
            text = ' '.join(paragraphs)
            #Helps to save special characters before the purge
            text = text.replace(':', ': ').replace('!', '! ').replace('?', '? ').replace('. . .', '...').replace('1',
                                                                                                                 '1 ').replace(
                   '2', '2 ').replace('3', '3 ').replace('4', '4 ').replace('5', '5 ').replace('6','6 ').replace('7',
                                                                                                                 '7 ').replace(
                   '8', '8 ').replace('9', '9 ').replace('0', '0 ').replace('!  ', '! ').replace('?  ','? ').replace(':  ',
                                                                                                                     ': ').replace(
                   ';', '; ').replace(';  ', '; ')
            text = bytes(text, 'utf-8').decode('unicode_escape').encode('ascii', 'ignore').decode('utf-8')
            print(text)
            #Say it for me, baby.
            say(text)
        input("End of Line.")
    
    elif 'fanfiction' in text and 'wattpad' not in text:
        #Loop through each chapter in a fanfiction and save the audio reading of each
        while 1:
            url = text.split('/')
            text = parse_it(get_story_fanfiction(text))
            #Set up the name for each audio recording
            title = url[-1].replace('-',' ') + ' ' + url[-2]
            print(text)
            text = text.replace('\n', ' ').replace('\r', ' ').replace('.','. ').replace('Klenon','Klenn une').replace('Tali','Tahlie').replace('tali','tahlie').replace ('Yalo',' Yah-lo ').replace('Noveria',' No-veir-eaah ').replace('Binary','Bi-nary')
            say(text,title)
            #Iterate to the next chapter and reset the URL
            url[-2] = str(int(url[-2]) + 1)
            text = '/'.join(url)
    
    elif 'pdf' in text:
        def getText(path,page):
            return parse_it(PyPDF2.PdfFileReader(path).getPage(page).extractText().replace('\u2122',"'"))
    
        try: #Safety first!
            os.remove(os.getcwd() + '\\PDF2BEREAD.pdf')
        except:
            pass
    
        if 'http://' in text or 'https://' in text:
            #Download the PDF from the web
            path = urlopen(text)
            file = open('PDF2BEREAD.pdf','wb')
            file.write(path.read())
            file.close()
            path = os.getcwd() + '\\PDF2BEREAD.pdf'
        first_page = int(input("Please enter the beginning page: ")) - 1
        for each_page in range(first_page,PyPDF2.PdfFileReader(path).getNumPages()):
            text = getText(path,each_page)
            print('\n \t \t' + str(each_page + 1) + '\n')
            print(text)
            text = text.replace("\'", '').replace('\"', '').replace('\n', ' ').replace('Klenon','Klenn une').replace('Tali','Tahlie').replace('tali','tahlie').replace ('Yalo',' Yah-lo ').replace('Noveria',' No-veir-eaah ').replace('Binary','Bi-nary').replace('Garrus','Gae-rrus').replace('Vakarian','Vah-kare-eean')
            say(text)
        input("End of line.")
    
    elif 'deviantart' in text.lower():
        text = get_story(text)
        print(text)
        say(text)
        input("End of line.")
    
    else:
        print(text)
        text = text.replace("\'", '').replace('\"', '').replace('\n', ' ').replace('Klenon','Klenn une').replace('Tali','Tahlie').replace('tali','tahlie').replace ('Yalo',' Yah-lo ').replace('Garrus','Gae-rrus').replace('Vakarian','Vah-kare-eean').replace('Noveria',' No-veir-eaah ').replace('Binary','Bi-nary')
        say(text)
        input("End of line.")


say("Initializing...")
text = input('State your request, creator: ')
OmniReader(text)