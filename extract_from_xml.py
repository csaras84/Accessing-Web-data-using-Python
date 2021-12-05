import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url-')
data = urllib.request.urlopen(url, context=ctx).read().decode()



tree = ET.fromstring(data)

lst = tree.findall('comments/comment/count')
sum = 0
c = 0
for item in lst:
    c = c+1
    sum = sum+int(item.text)
print('Count is:', c)
print('Sum is:', sum)
