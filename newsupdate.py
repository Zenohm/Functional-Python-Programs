def main():
	subject = input("What subject should be checked? ")
	number_of_results = input("How many results should be returned? ")
	data = newsupdate(subject,number_of_results)
	for files in data:
		try:	
			print(files['TITLE'] + ' : ' + files['TEASER'])
		except:
			print("Return failed. Proceeding.")

def newsupdate(subject,number_of_results):
	from urllib.request import urlopen
	import json, codecs
	url = 'http://api.npr.org/query?apiKey='
	key = 'MDE4MTgxNDcwMDE0MjMxNzM2NjQ1ODJhOQ001'
	url += key + '&numResults={}'.format(number_of_results) + '&format=json&id='
	url += 'requiredAssets=text'
	try:
		url += subjectcode(subject)
	except:
		return "Subject not found."
	reader = codecs.getreader("utf-8")
	response = urlopen(url)
	json_obj,stories = json.load(reader(response)),[]
	for story in json_obj['list']['story']:
		story_text = []
		for paragraph in story['textWithHtml']['paragraph']:
			story_text.append(paragraph['$text']+"\n")
		stories.append({"TITLE":story['title']['$text']+"\n","DATE":story['storyDate']['$text']+"\n","TEASER":story['teaser']['$text']+"\n","TEXT":story_text})
	return stories

def subjectcode(name):
	name,list = name.title(),[]
	import xml.etree.ElementTree as ET
	root = ET.parse('list.id=3002.txt').getroot()
	for child in root:
		list.append(child.attrib)
	for iterations in range(1,len(root)-1):
		if name == root[iterations][0].text:
			return list[iterations]['id']
