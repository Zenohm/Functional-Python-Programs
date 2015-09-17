#Crawling webpages
from urllib.request import urlopen
from time import sleep
from bs4 import BeautifulSoup as BS
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
def nothings(input):
 response = str(BS(urlopen(url+str(input))).text)
 for each_try in range(input+400):
  try:
   response = str(BS(urlopen(url+str([int(s) for s in response.split() if s.isdigit()][0]))).text);print(str([int(s) for s in response.split() if s.isdigit()][0]))
  except:
   return("Non-Nothing URL found!", response)


#Crawling text files
url = "C:/Users/Isaac/Desktop/channel/"
def nothings(input=90052):
 response = str(open(url+str(input)+'.txt').read())
 for each_try in range(input+40000):
  try:
   response = str(open(url+str([int(s) for s in response.split() if s.isdigit()][0])+'.txt').read())
   print(str([int(s) for s in response.split() if s.isdigit()][0]))
  except:
   return("Non-Nothing URL found!", response)

#Crawling zip files
import zipfile
comments = []
commadd = comments.append
myzip = zipfile.ZipFile('C:/Python34/channel.zip')
def nothings(input=90052):
 response = myzip.open(str(input)+'.txt').read().decode('utf-8')
 commadd(myzip.getinfo(str(input)+'.txt').comment.decode('utf-8'))
 for each_try in range(input+40000):
  try:
   response = myzip.open(str([int(s) for s in response.split() if s.isdigit()][0])+'.txt').read().decode('utf-8')
   commadd(myzip.getinfo(str(input)+'.txt').comment.decode('utf-8'))
   print(str([int(s) for s in response.split() if s.isdigit()][0]))
  except:
   print(commadd)
   return("Non-Nothing URL found!", response)
