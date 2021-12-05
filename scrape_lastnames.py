import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL -')
count = int(input('Enter count:'))
pos = int(input('Enter position:'))

print('Retrieving:', url)


while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    c = 0
    p = 0

    for tag in tags:
        p = p + 1
        if p == pos:
            print('Retrieving:', str(tag.get('href', None)))
            url = str(tag.get('href', None))
            p = 0
            break

    count = count - 1
