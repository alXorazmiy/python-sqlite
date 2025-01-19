import os
import sqlite3

script_path = os.path.abspath(__file__)
dir_path = os.path.dirname(script_path)


db = sqlite3.connect(f"{dir_path}/database/Mydb.db")
cursor = db.cursor()


# cursor.execute("SELECT age, COUNT(*) FROM users GROUP BY age")
# cursor.execute("SELECT name, COUNT(*) FROM users GROUP BY name")
# cursor.execute("SELECT name, COUNT(*) FROM users GROUP BY name HAVING COUNT(*)>1")

# cursor.execute("SELECT age, SUM(age) FROM users GROUP BY age")


# cursor.execute("SELECT age, MIN(age) FROM users GROUP BY age")
cursor.execute('''SELECT age, COUNT(*), AVG(age), MIN(age), MAX(age) 
        FROM users 
        GROUP BY age 
        HAVING COUNT(*) > 1 
        ORDER BY age'''
)



rows = cursor.fetchall()
for row in rows:
    print(row)




db.close()
