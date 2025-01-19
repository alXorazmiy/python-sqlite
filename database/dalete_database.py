import sqlite3
import os

script_path = os.path.abspath(__file__)
directory_path = os.path.dirname(script_path)

database = sqlite3.connect(f"{directory_path}/database/mydatabase.db")
cursor = database.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
               id  INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER
    )
''')
database.commit()


cursor.execute("DELETE FROM users WHERE id = ?", (3,))
database.commit()


cursor.execute("SELECT *FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)





cursor.close()
database.close()