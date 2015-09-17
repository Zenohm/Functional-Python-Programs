def schoolStatus():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    try:
        soup = BeautifulSoup(urlopen('http://www.ph.k12.in.us/'))
    except:
        return "Unable to connect."
    text = str(soup.html.body.div.text)
    if "School is Open" in text:
        return 1
    elif "2 hour" in text:
        return 2
    elif "3 hour" in text:
        return 3
    else:
        return 0
