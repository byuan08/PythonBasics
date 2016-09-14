import sqlite3
import urllib

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Read from file on disk
fname = raw_input('Enter File Name: ')

if len(fname)<1: 
	fname = 'mbox-short.txt'
	print('Using default shortened file as default')
fd = open(fname, 'r')

for line in fd:
	if line.startswith('From:'):
		l = line.split()
		email = l[1]
		org = email.split('@')[1]
		#print(domain)
		#org = domain.split('.')[0]
		#print(org)
		cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
		row = cur.fetchone()
		if row is None:
			cur.execute('INSERT INTO Counts (org, count) VALUES (?,1)', (org,))
		else:
			cur.execute('UPDATE Counts SET count = count+1 WHERE org = ?',(org,))

conn.commit()

row = cur.execute('SELECT org, count FROM Counts ORDER BY count DESC Limit 1')

# row is iterator
result = next(row)

print(str(result[0]),result[1])
cur.close()








