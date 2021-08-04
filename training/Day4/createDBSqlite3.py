
import sqlite3

conn = sqlite3.connect("students.db")

conn.commit()

conn.close()