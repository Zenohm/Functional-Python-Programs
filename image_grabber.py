def image_open(url):
    from PIL import Image
    from urllib.request import urlopen
    import io
    if 'http' not in url:
        url = 'https://'+url
    
    fd = urlopen(url)
    image_file = io.BytesIO(fd.read())
    im = Image.open(image_file)
    im.show()


def get_image_urls(url):
    import urllib.request
    from bs4 import BeautifulSoup
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html)
    links = soup.findAll('img', src=True)
    if '/' != url[:-1]:
        url+='/'
    links = [link['src'] for link in links]
    for link in links:
        if 'http' != link[0:3]:
            link = url+link
    return links

def load():
    data = urllib.request.urlopen(ROOT_URL + 'archivepix.html').read()
    soup = BeautifulSoup(data, 'lxml')
    results = soup.find('b').findAll('a')
    urls = [result['href'] for result in results]
    return urls
