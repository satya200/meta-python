
import psycopg2

conn = psycopg2.connect(host='localhost', user='postgres', password='root', port='5432')

conn.autocommit = True

cursor = conn.cursor()

cursor.execute("create database students")

conn.close()

