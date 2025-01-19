import os
import sqlite3

script_path = os.path.abspath(__file__)
dir_path = os.path.dirname(script_path)


db = sqlite3.connect(f"{dir_path}/database/Mydb.db")
cursor = db.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        amount REAL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )'''
)
db.commit()




cursor.execute("INSERT INTO orders (user_id, amount) VALUES(?, ?)", (1, 9900.0))
db.commit()




db.close()
