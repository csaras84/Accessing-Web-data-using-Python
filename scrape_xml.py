import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Saraswathi</name>
  <phone type = "intl">
    +91987654387
  </phone>
  <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
