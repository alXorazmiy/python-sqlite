import sqlite3
import os

script_path = os.path.abspath(__file__)
directory_path = os.path.dirname(script_path)

database = sqlite3.connect(f"{directory_path}/database/mydatabase.db")
cursor = database.cursor()