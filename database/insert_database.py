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


name = input("Ismni kiriting: ")
age = int(input("Yoshni kiriting: "))
cursor.execute("INSERT INTO users(name, age) VALUES(?,?)", (name, age))
database.commit()





cursor.close()
database.close()