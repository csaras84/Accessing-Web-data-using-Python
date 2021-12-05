import xml.etree.ElementTree as ET

data = '''
<stuff>
  <users>
    <user x="2">
        <id>001</id>
        <name>Saraswathi</name>
    </user>
    <user x="7">
        <id>002</id>
        <name>Julie</name>
    </user>
  </users>
</stuff>'''

tree = ET.fromstring(data)

lst = tree.findall('users/user')
print('User Count:', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attr:', item.get('x'))
