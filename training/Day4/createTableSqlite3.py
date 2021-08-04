
import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

query = """
    create table students (
    studid varchar(4) PRIMARY KEY,
    studname varchar(50) not null,
    age integer not null,
    class varchar(5) not null
    )
"""

cursor.execute(query)

conn.commit()
conn.close()
