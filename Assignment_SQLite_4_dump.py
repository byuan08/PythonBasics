import sqlite3, json
import subprocess

subprocess.call(['clear'])

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

fd = open('where.js', 'w')
fd.write('myData = [\n')

# return the entire table with all rows and columns
cur.execute('''SELECT * FROM Locations''')

for row in cur:
	#print 'row:' + str(row[1])
	data = json.loads(str(row[1]))

	try:
		lat = data['results'][0]['geometry']['location']['lat']
		lng = data['results'][0]['geometry']['location']['lng']
		addr = data['results'][0]['formatted_address']
		addr = addr.replace("'","")
		jsline = "[" + str(lat) + ", "+ str(lng) + ", '" + addr + "'],"
		print jsline
		fd.write(jsline)
		fd.write('\n')

	except:
		print 'No data found in database'
		continue
cur.close()
fd.write("];\n")
fd.close


