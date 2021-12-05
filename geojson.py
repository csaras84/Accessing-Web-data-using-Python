import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    addr = input('Enter location-')
    if len(addr) < 1:
        break

    #Google maps api rule for forming actual link
    url = serviceurl + urllib.parse.urlencode({'address' : addr})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    #error handling in case of problem with data Retrieved
    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failure to Retreive')
        print(data)
        continue

    #prettify
    print(json.dumps(js, indent = 4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lon = js["results"][0]["geometry"]["location"]["lng"]

    location = js['results'][0]['formatted address']
    print(location)
