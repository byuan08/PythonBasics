
#!/usr/local/bin/python3

import urllib.request
import xml.etree.ElementTree as ET

my_url = 'http://python-data.dr-chuck.net/comments_261936.xml'

xml_data = urllib.request.urlopen(my_url).read()

#print(xml_data)

xml_tree = ET.fromstring(xml_data)
results = xml_tree.findall('.//count')
#print(results)

total = 0
for count in results:
	ct = int(count.text)
	total += ct

print('total =',total)
