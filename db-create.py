#sqlite3 to create database for us
import sqlite3

db_locale = 'users.db'
connie = sqlite3.connect(db_locale)
c=connie.cursor()

#command
c.execute("""
	CREATE TABLE comments_data
	(id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	title TEXT,
	comment TEXT
	)
	""")
connie.commit()
connie.close()