def parse_json(url):
    from bs4 import BeautifulSoup as BS
    from json import loads
    from urllib.request import urlopen
    return loads(BS(urlopen(url)).text)

