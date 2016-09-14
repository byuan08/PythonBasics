import json
import sqlite3
import subprocess

subprocess.call(['clear'])

conn = sqlite3.connect('roster_data.sqlite')
cur = conn.cursor()

cur.executescript('''
	DROP TABLE IF EXISTS User;
	DROP TABLE IF EXISTS Course;
	DROP TABLE IF EXISTS Member;

	CREATE TABLE User (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
				 	   name TEXT UNIQUE);
	CREATE TABLE Course (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
						 name TEXT UNIQUE);
	CREATE TABLE Member (user_id INTEGER,
						 course_id INTEGER,
						 role INTEGER,
						 PRIMARY KEY (user_id, course_id)) 


''')

#fname = raw_input('Enter File Name: ')
fname = 'roster_data.json'
text = open(fname).read()
jlist = json.loads(text)

for entry in jlist:
	user = entry[0]
	course = entry[1]
	role = entry[2]

	cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''', (user,))
	cur.execute('''SELECT id FROM User WHERE name = ?''', (user,))
	user_id = cur.fetchone()[0]
	#print user_id
	cur.execute('''INSERT OR IGNORE INTO Course (name) VALUES (?)''', (course,))
	cur.execute('''SELECT id FROM Course WHERE name = ?''', (course,))
	course_id = cur.fetchone()[0]
	#print course_id
	cur.execute('''INSERT OR REPLACE INTO Member(user_id, course_id, role) VALUES (?, ?, ?)''',
		(user_id, course_id, role,))
	conn.commit()

