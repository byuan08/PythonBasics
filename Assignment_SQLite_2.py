import sqlite3
import xml.etree.ElementTree as ET
import os
import subprocess

subprocess.call(['clear'])
#subprocess.call(['touch', 'tracks.sqlite'])


conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()
cur.executescript('''

 	DROP TABLE IF EXISTS Artist;
 	DROP TABLE IF EXISTS Genre;
 	DROP TABLE IF EXISTS Album;
 	DROP TABLE IF EXISTS Track;

	CREATE TABLE Artist(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT UNIQUE);

	CREATE TABLE Genre(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT UNIQUE);

	CREATE TABLE Album(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT UNIQUE,
	artist_id INTEGER);

	CREATE TABLE Track(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT UNIQUE,
	len INTEGER,
	rating INTEGER,
	count INTEGER,
	album_id INTEGER,
	genre_id INTEGER);

''')

cwd  = os.getcwd()
rel_path = 'tracks/Library.xml'
abs_path = os.path.join(cwd, rel_path)
print abs_path

fname = abs_path
def lookup(d, key):
	found = False
	for child in d:
		if found: return child.text
		if child.tag == 'key' and child.text == key:
			found = True
	return None

xml = ET.parse(fname)
all_stuff = xml.findall('dict/dict/dict')
print 'Dict Count:', len(all_stuff)
ct = 0
for entry in all_stuff:
	if (lookup(entry, 'Track ID') is None): continue


	name = lookup(entry,'Name')
	#print 'name:',  name
	artist = lookup(entry, 'Artist')
	album = lookup(entry, 'Album')
	genre = lookup(entry, 'Genre')
	count = lookup(entry, 'Count')
	rating = lookup(entry, 'Rating')
	length = lookup(entry, 'Length')



	if name is None or artist is None or album is None or genre is None: continue

	cur.execute('''
		INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist, ))
	cur.execute('''
		SELECT id FROM Artist WHERE name = ?''', (artist,))
	artist_id = cur.fetchone()[0]


	cur.execute('''
		INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre, ))
	cur.execute('''
		SELECT id FROM Genre WHERE name = ?''', (genre,))
	genre_id = cur.fetchone()[0]
	# try: genre_id = cur.fetchone()[0]
	# except: genre_id = -1


	cur.execute('''
		INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?,?)''', (album, artist_id))
	cur.execute('''
		SELECT id FROM Album WHERE title = ?''', (album,))
	album_id = cur.fetchone()[0]

	cur.execute('''
		INSERT OR REPLACE INTO Track (title, len, rating, count, album_id, genre_id) VALUES (?, ?, ?, ?, ?, ?)''', (name, length, rating, count, album_id, genre_id, ))

	conn.commit()



