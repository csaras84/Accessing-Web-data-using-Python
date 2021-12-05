import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter address-')

parms = dict()
parms['address'] = address

if api_key is not False:
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
print(url)

uh = urllib.request.urlopen(url, context = ctx)
data = uh.read().decode()
js = json.loads(data)
#print(json.dumps(js, indent =4))
location = js['results'][0]['place_id']
print(location)
