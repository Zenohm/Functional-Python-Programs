import os
import time
from subprocess import call
from platform import python_version
home = os.path.expanduser("~")


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



speech_system = 'google'
def say(message,title='Speak',speech_system='google'):
    if speech_system == 'google':
        try:
            # Create the MP3 file which will speak the text
            title += '.mp3'
            tts = gTTS(message)
            tts.save(home+'\\'+title)
            if title == 'Speak':
                os.system("start /MIN {}".format(home+'\\'+title))
        except:
            print("Vocalization failed.")
    else:
        try:
            # Create the Visual Basic code which will speak the text
            with open(title + '.vbs', 'w') as file:
                file.write(
                        """speaks="{}"\n
                           Dim speaks, speech\n
                           Set speech=CreateObject("sapi.spvoice")\n
                           speech.Speak speaks""".format( str(message) ))
            # Execute the file
            call(['cscript.exe', title + '.vbs'])
        except:
            print("Vocalization failed.")


class getStory:
    def __init__(self,url):
        self.url = url
        self.speech = speech_system
        self.text = 'Please initialize.'
        if 'wattpad' in self.url:
            self.type = 'wattpad'
        elif 'fanfiction' in self.url and 'wattpad' not in self.url:
            self.type = 'fanfiction'
        elif 'deviantart' in self.url:
            self.type = 'deviantart'
        elif 'pdf' in self.url:
            self.type = 'pdf'
        else:
            self.type = 'text'
        if 'http://' in url or 'https://' in url:
            self.pathtype = 'url'
        else:
            self.pathtype = 'local'
        
    def initialize(self):
        if self.type == 'wattpad':
            self.wattpad()
        elif self.type == 'fanfiction':
            self.fanfiction()
        elif self.type == 'deviantart':
            self.deviantart()
        elif self.type == 'pdf':
            self.pdf_inititialize()
        else:
            pass
        
    def fanfiction(self):
        # Opens and parses the URL with BeautifulSoup
        soup = BeautifulSoup(urlopen(str(self.url)))
        # Finds the path and contents given by the search
        try:
            self.text = soup.find(class_='storytext').text
        except:
            print('Retrieval Failed.')
        
    def deviantart(self):
        try:
            soup = BeautifulSoup(urlopen(str(self.url)))
            self.text = soup.select('#devskin > div > div > div.gr-body > div > div > div')[0].text
        except:
            print('Retrieval Failed.')
        
    def wattpad(self, page=0, mode='singular'):  # Modes are singular and plural
        if page:
            page = '/page/' + str(page)
        else:
            page = ''
        #Opens and parses the URL with BeautifulSoup
        soup = BeautifulSoup(urlopen(str(self.url + page)))
        #Finds the path and contents given by the search
        if mode == 'singular':
            self.text = soup.find(class_="panel panel-reading")
        elif mode == 'plural':
            self.text = soup.find_all(class_="panel panel-reading")
        
    def pdf_inititialize(self):
        try: #Safety first!
            os.remove(os.getcwd() + '\\PDF2BEREAD.pdf')
        except:
            pass
        if self.pathtype == 'url':
            #Download the PDF from the web
            path = urlopen(self.url)
            with open('PDF2BEREAD.pdf','wb') as file:
                file.write(path.read())
            self.url = os.getcwd() + '\\PDF2BEREAD.pdf'
    
    def pdf(self,page):
        self.text = PyPDF2.PdfFileReader(self.url).getPage(page).extractText().replace('\u2122',"'")
    
    def text(self):
        self.text = self.url
    
    def parse(self):
        #Removes all unicode characters, nonprintable characters, and HTML code
        text = str(bytes(self.text,'utf-8').decode('unicode_escape').encode('ascii','ignore').decode('utf-8'))
        #Removes newline and return characters
        if speech_system == 'local':
            self.text = text.replace('\n',' ').replace('\r',' ').replace('"',"'").replace('.','. ').replace('.   .   . ','').replace("\'", '').replace('\"', '').replace('Klenon','Klenn une').replace('Tali','Tahlie').replace('tali','tahlie').replace ('Yalo',' Yah-lo ').replace('Garrus','Gae-rrus').replace('Vakarian','Vah-kare-eean').replace('Noveria',' No-veir-eaah ').replace('Binary','Bi-nary').replace('caf ', 'cafe ')
        else:
            self.text = text.replace('\n',' ').replace('\r',' ').replace('"',"'").replace('.','. ').replace('.   .   . ','').replace("\'", '').replace('\"', '').replace('Tali','Tahhlee').replace('tali','Tahhlee').replace('caf ', 'cafe ')

def OmniReader(text):
    story = getStory(text)
    
    if story.type == 'wattpad':
        number_of_pages = int(input("How many pages are in the story: ")) + 1
        # Iterates through the pages of the story
        for each_page in range(number_of_pages):
            if each_page:
                #Designed to cope with Wattpad's fucking weird multi-page system
                story.wattpad(each_page,'plural')[1]
            else:
                #Meant for the first page because fuck Wattpad
                story.wattpad()
            #Get all the text in one big orgy array
            paragraphs = story.text.find_all('p')
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
            say(text,speech_system=speech_system)
        input("End of Line.")
        
    elif story.type == 'fanfiction':
        #Loop through each chapter in a fanfiction and save the audio reading of each
        try:
            while 1:
                url = story.url.split('/')
                story.fanfiction()
                #Set up the name for each audio recording
                title = url[-1] + '_' + url[-2]
                story.parse()
                print(story.text)
                say(story.text,title,speech_system)
                #Iterate to the next chapter and reset the URL
                url[-2] = str(int(url[-2]) + 1)
                story.url = '/'.join(url)
        except:
            input("End of Line.")
        
    elif story.type == 'pdf':
        first_page = int(input("Please enter the beginning page: ")) - 1
        for each_page in range(first_page,PyPDF2.PdfFileReader(self.url).getNumPages()):
            story.pdf(each_page)
            print('\n \t \t' + str(each_page + 1) + '\n')
            print(story.text)
            story.parse()
            say(story.text,speech_system=speech_system)
        input("End of line.")
        
    elif story.type == 'deviantart':
        story.deviantart()
        url = story.url.split('/')
        title = url[-1]
        story.parse()
        print(story.text)
        say(story.text,title,speech_system)
        input("End of line.")
        
    elif story.type == 'text':
        print(story.url)
        story.text()
        story.text = story.url
        story.parse()
        say(story.text,speech_system=speech_system)
        input("End of line.")

try:
    say("Initializing...")
except:
    speech_system = 'local'

text = input("State your request, creator: ")
OmniReader(text)
