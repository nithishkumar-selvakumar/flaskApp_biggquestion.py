#sqlite3 to create database for us
import sqlite3
db_locale = 'users.db'
connie = sqlite3.connect(db_locale)
c=connie.cursor()

#command
c.execute("""
	SELECT * FROM comments_data
	""")

user_info=c.fetchall()
print(user_info)
for user in user_info:
	print(user)
connie.commit()
connie.close()