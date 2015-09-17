import math
import os
import sys


def time_convert(time_in_seconds):
	units = 'seconds'
	if time_in_seconds//1 == 0:
		#Subsecond conversions first
		if time_in_seconds <= 0.000000000000000000000001:
			time_in_seconds /= 0.000000000000000000000001
			units = 'yoctoseconds'
		elif time_in_seconds <= 0.000000000000000000001:
			time_in_seconds /= 0.000000000000000000001
			units = 'zeptoseconds'
		elif time_in_seconds <= 0.000000000000000001:
			time_in_seconds /= 0.000000000000000001
			units = 'attoseconds'
		elif time_in_seconds <= 0.000000000000001:
			time_in_seconds /= 0.000000000000001
			units = 'femtoseconds'
		elif time_in_seconds <= 0.000000000001:
			time_in_seconds /= 0.000000000001
			units = 'picoseconds'
		elif time_in_seconds <= 0.000000001:
			time_in_seconds /= 0.000000001
			units = 'nanoseconds'
		elif time_in_seconds <= 0.000001:
			time_in_seconds /= 0.000001
			units = 'microseconds'
		elif time_in_seconds <= 0.001:
			time_in_seconds /= 0.001
			units = 'milliseconds'
		elif time_in_seconds <= 0.01:
			time_in_seconds /= 0.01
			units = 'centiseconds'
	else:
		#Supersecond conversions last
		if time_in_seconds >= 440294400000000000:
			time_in_seconds /= 440294400000000000
			units = 'ages-of-the-universe'
		elif time_in_seconds >= 31449600000:
			time_in_seconds /= 31449600000
			units = 'millennia'
		elif time_in_seconds >= 3144960000:
			time_in_seconds /= 3144960000
			units = 'centuries'
		elif time_in_seconds >= 31449600:
			time_in_seconds /= 31449600
			units = 'years'
		elif time_in_seconds >= 604800:
			time_in_seconds /= 604800
			units = 'weeks'
		elif time_in_seconds >= 86400:
			time_in_seconds /= 86400
			units = 'days'
		elif time_in_seconds >= 3600:
			time_in_seconds /= 3600
			units = 'hours'
		elif time_in_seconds >= 60:
			time_in_seconds /= 60
			units = 'minutes'
	return str(time_in_seconds) + ' ' + units

def passwordpower(password):
	if not password.strip():
		return 'An input is required in order to be analyzed.'
	
	passwordscore, entropypool, characters, response = 0, 0, list(password), False

	results = {'uppercase':0,
			   'lowercase':0,
			   'numbers':0,
			   'special':0}

	powercheck = {'uppercase':'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
			      'lowercase':'abcdefghijklmnopqrstuvwxyz',
				  'numbers':'1234567890',
				  'special':""" `~!@#$%^&*()_-+={[]}|\:;"'<,>.?/*"""}

	for currentcharacter in characters:
		for currentcheck in powercheck:
			if currentcharacter in powercheck[currentcheck]:
				results['{}'.format(currentcheck)] += 1
	
	try:
		commonpasswordslist = ''.join([p.replace('\n',' ') for p in open(os.path.join(os.path.split(sys.argv[0])[0],'10k most common.txt'),'r')]).split()
	except:
		commonpasswordslist = ''

	length,entropypool = 1,1

	if password in commonpasswordslist:
		response = True
		entropypool,length = 10000,1
		for currentscore in results:
			if results[currentscore]:
				passwordscore += 1
	else:
		length = len(password)
		for currentscore in results:
			if results[currentscore]:
				passwordscore += 1
				entropypool += len(powercheck['{}'.format(currentscore)])

	if not passwordscore:
		passwordscore += 1

	approximate_max_time_to_compute = time_convert((2**(length*math.log(entropypool)))/350000000000)
	bitentropy = length*math.log(entropypool,2)
	PowerAcclimationRatio = 1000*float(approximate_max_time_to_compute.split()[0])/(passwordscore*length*math.log(entropypool,2))
	rankings = {'ages-of-the-universe':"Crackers' Bane",
			    'millennia':'Extremely Secure',
				'centuries':'Very Secure',
				'years':'Secure',
				'weeks':'Mediocre Security',
				'days':'Insecure',
				'hours':'Very Insecure',
				'minutes':'Extremely Insecure',
				'seconds':'Dangerously Insecure'}
	
	try:
		safetysticker = rankings['{}'.format(approximate_max_time_to_compute.split()[1])]
	except:
		safetysticker = "Instantaneous Cracking"
	
	if response:
		safetysticker = 'This is one of the 10,000 most used passwords, it would be cracked almost instantaneously.'

	if not commonpasswordslist:
		response = 'Unknown'

	statistics = {'score':passwordscore,
			      'length':len(password),
				  'common':response,
				  'bitentropy':bitentropy,
				  'maxtime':approximate_max_time_to_compute,
				  'PowerAcclimationRatio':PowerAcclimationRatio,
				  'Safety':safetysticker}

	print("\n--Scores--\n\n"
	      "Power-Acclimation Ratio: {0}\n"
		  "Password Variety Score (Out of 4): {1}\n\n"
		  "--Password Information--\n\n"
		  "Bit Entropy: {2}\n"
		  "Password Length: {3}\n"
		  "Common: {4}\n"
		  "Maximum Time Required to Break Password: {5}\n"
		  "Password Safety: {6}\n".format(PowerAcclimationRatio,
										  passwordscore,
										  bitentropy,
										  len(password),
										  response,
										  approximate_max_time_to_compute,
										  safetysticker))

passwordpower(input('Please input a password to be analyzed: '))
input('End of Line.')