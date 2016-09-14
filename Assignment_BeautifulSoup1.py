import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:')
for i in range(1,8):

	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	anchorTags = soup('a')
	tag = anchorTags[17]
	name = tag.contents[0]
	url = tag.get('href', None)
	print name




