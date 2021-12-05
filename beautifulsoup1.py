import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter-')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all anchor tags
tags = soup('a')

for tag in tags:
    #pull out href key or None
    print(tag.get('href', None))
