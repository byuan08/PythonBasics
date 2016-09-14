import urllib
from BeautifulSoup import *
import re

url = raw_input('Enter URL:')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

spanTags = soup('span')
#print spanTags
total = 0
for tag in spanTags:
	#print 'URL:',tag.contents[0]

	num = int(tag.contents[0])

	total += num

print total
