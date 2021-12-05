import urllib.request, urllib.parse, urllib.error
import ssl
import json

#ignore ssl cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url-')

data = urllib.request.urlopen(url, context = ctx).read().decode()
info = json.loads(data)
#print(info)
my_sum = 0
#print(type(info))
#print(len(info))

#print(json.dumps(info, indent=2))

for item in info['comments']:
    my_sum = my_sum+int(item['count'])

print(my_sum)
