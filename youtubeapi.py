from bs4 import BeautifulSoup
from urllib.request import urlopen
import string

def filter_nonprintable(text):
    # Get the difference of all ASCII characters from the set of printable characters
    nonprintable = set([chr(i) for i in range(128)]).difference(string.printable)
    # Use translate to remove all non-printable characters
    return text.translate({ord(character):None for character in nonprintable})

def wtf_dat(url):
    soup = BeautifulSoup(urlopen(str(url)))
    info = soup.find(class_='watch-main-col ')
    info = info.find(class_="watch-title ")
    title = info['title']
    desc = soup.find(id='eow-description').text
    return {'title'      :title,
            'description':desc}

data = wtf_dat(input("Please input a youtube URL: "))
print("\nVideo Title: \n\n", data['title'])
print("\n\n\n")
print("Description: \n\n", filter_nonprintable(data['description']))
input("End of line.")
