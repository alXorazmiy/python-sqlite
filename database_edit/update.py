import os
import sqlite3

script_path = os.path.abspath(__file__)
dir_path = os.path.dirname(script_path)


db = sqlite3.connect(f"{dir_path}/database/Mydb.db")
cursor = db.cursor()



cursor.execute("CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
db.commit()


# cursor.execute("ALTER TABLE users ADD COLUMN email TEXT")
cursor.execute("ALTER TABLE users ADD COLUMN phone TEXT")
db.commit()




db.close()
