#sqlite3 to create database for us
import sqlite3
db_locale = 'users.db'
connie = sqlite3.connect(db_locale)
c=connie.cursor()

#command
c.execute("""
	DELETE FROM comments
	

	""")

connie.commit()
connie.close()