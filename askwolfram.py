def askwolfram():
	import SpeechRecognitionAsk as sra
	import wolfquery,say
	question = sra.ask()
	print(question)
	response = wolfquery.wolfquery(question)
	say.say(response)
	return response
