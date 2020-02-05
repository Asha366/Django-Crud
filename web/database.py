import sqlite3

#Open database
conn = sqlite3.connect('db.sqlite3')

#Create table
conn.execute('''CREATE TABLE members
		(userId INTEGER PRIMARY KEY,
		firstName TEXT,
		lastName TEXT,
		phone TEXT
		)''')

conn.close()

