import json
import urllib

url = raw_input('Enter URL:')
jstr = urllib.urlopen(url).read()

dict_str = json.loads(jstr)
#print(dict_str)

comments = dict_str['comments']
total = 0
for obj in comments:
	count = obj['count']
	total += int(count)

print(total)

	
