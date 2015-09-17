def ask():
	import speech_recognition as sr
	r = sr.Recognizer()
	count = 4
	while count > 0:
		print("Please speak now")
		with sr.Microphone() as source:
			audio = r.listen(source)
		print("Processing audio")
		try:
			return r.recognize(audio)  # recognize speech using Google Speech Recognition
		except LookupError:            # speech is unintelligible
			print("Could not understand audio")
			count -= 1
			print("{} attempts remaining".format(count))
	return "Audio could not be decyphered"