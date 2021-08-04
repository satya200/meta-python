
import psycopg2
conn = psycopg2.connect(database='students', user='postgres', password='root', host='localhost',
                        port='5432')

query = "select * from students"

cursor = conn.cursor()

cursor.execute(query)

for rec in cursor.fetchall():
    print(*rec)

conn.close()
