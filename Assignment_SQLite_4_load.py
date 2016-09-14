import urllib, sqlite3, json
import subprocess, time

subprocess.call(['clear'])

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
scontext = None

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Locations 
				(address TEXT, geodata TEXT)''')

fd = open('./geodata/where.data', 'r')
for line in fd:
	location = line.strip()
	cur.execute('''SELECT geodata FROM LOCATIONS WHERE address = ?''', (location,))
	try: 
		cur.fetchone()[0]
		print 'Found in database: ', location
		continue
	except: 
		pass

	url = serviceurl + urllib.urlencode({'sensor':'false', 'address':location})
	print url
	uh = urllib.urlopen(url, context = scontext)
	data = uh.read()



	try:
		#js = json.loads(str(data))
		js = json.loads(str(data))

	except:
		print 'invalid json data'
		continue

	print 'Retrieving ' + location + '...' 
	

	if 'status' not in js or js['status'] != 'OK':
		print '===== Failure on JSON Data Retrieval ====='
		print data
		continue
	else:

		cur.execute('''INSERT INTO Locations (address, geodata) VALUES (?, ?)''', 
			(buffer(location), buffer(data)))

	conn.commit()
	time.sleep(1)

fd.close()




				

