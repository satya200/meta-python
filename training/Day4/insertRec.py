
import psycopg2
conn = psycopg2.connect(database='students', user='postgres', password='root', host='localhost',
                        port='5432')
conn.autocommit = True

cursor = conn.cursor()

query = "insert into students values ('S005', 'Jane', 9, 'IV')"

cursor.execute(query)

conn.close()
