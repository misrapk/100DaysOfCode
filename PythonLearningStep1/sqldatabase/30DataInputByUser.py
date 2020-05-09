import sqlite3 as sql

con= sql.connect(":memory:")   #with this we can overwrite the existing db
cur = con.cursor()
cur.execute("CREATE TABLE person (name, age, id)")

print("Enter 4 students names:")
sName = [input() for i in range(4)]
print("Enter their ages: ")
sAge = [int(input()) for i in range(4)]
print("Enter thier ids :")
sId = [int(input()) for i in range(4)]

n = len(sName)

for i in range(n):
	cur.execute("INSERT INTO person VALUES (?, ?, ?)", (sName[i], sAge[i], sId[i]))

	cur.execute("select * from person")

	print(cur.fetchall())

