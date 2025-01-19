import os
import sqlite3

script_path = os.path.abspath(__file__)
dir_path = os.path.dirname(script_path)


db = sqlite3.connect(f"{dir_path}/database/Mydb.db")
cursor = db.cursor()



# cursor.execute("SELECT * FROM users WHERE age > 25")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)


# cursor.execute("SELECT * FROM users WHERE name LIKE ?", ("Hus%",))
# rows = cursor.fetchall()

# for row in rows:
#     print(row)


# cursor.execute("SELECT * FROM users WHERE id =  ?", (3,))
# rows = cursor.fetchall()

# for row in rows:
#     print(row)


cursor.execute("SELECT * FROM users WHERE name IN (?, ?, ?)", ("Husniddin", "Asad", "Umar"))
rows = cursor.fetchall()

for row in rows:
    print(row)


# cursor.execute("SELECT * FROM users WHERE age BETWEEN 18 AND 25 ORDER BY age;")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)




db.close()
