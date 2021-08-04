
import psycopg2
conn = psycopg2.connect(database='students', user='postgres', password='root', host='localhost',
                        port='5432')
conn.autocommit = True

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
conn.close()
