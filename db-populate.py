#sqlite3 to create database for us
import sqlite3
db_locale = 'users.db'
connie = sqlite3.connect(db_locale)
c=connie.cursor()

#command
c.execute("""
	INSERT INTO comments_data (title,name,comment) VALUES 
	('what is?', 'nithish','its not a complete statement'),
	('42','blogs','its the new moviessss')

	""")

connie.commit()
connie.close()