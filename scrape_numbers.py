import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter-')
html = urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html, 'html.parser')

tags = soup('tr')
sum = 0
for tag in tags:
    a = str(tag)
    b = re.findall('[0-9]+', a)
    for i in b:
        sum+=int(i)
print(sum)
