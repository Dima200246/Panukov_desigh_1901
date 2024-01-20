import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="111", host="127.0.0.1")
cursor = conn.cursor()

conn.autocommit = True

sql = "CREATE DATABASE Panukov_desigh_0119"

cursor.execute(sql)
print("База данных успешно создана")

cursor.close()
conn.close()