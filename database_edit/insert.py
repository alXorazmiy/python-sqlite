import os
import sqlite3

script_path = os.path.abspath(__file__)
dir_path = os.path.dirname(script_path)


db = sqlite3.connect(f"{dir_path}/database/Mydb.db")
cursor = db.cursor()




cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ? )", ("Doston", 27, "Doston@gmail.com"))
db.commit()




db.close()
