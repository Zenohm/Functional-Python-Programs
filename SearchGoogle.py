import SpeechRecognitionAsk as sra
import webbrowser
query = sra.ask()
url = 'https://www.google.com.tr/search?q={}'.format(query)
webbrowser.open(url)