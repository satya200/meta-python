
import sqlite3
conn = sqlite3.connect('students.db')

cursor = conn.cursor()

query = "insert into students values ('S004', 'Mark', 10, 'Vth')"

cursor.execute(query)

conn.commit()
conn.close()