#code for updation and delteion in db
import sqlite3

conn = sqlite3.connect("mydatabase.db")

crsr = conn.cursor()
# SQL command to create a table in the database 
# sql_command = """CREATE TABLE student (  
# 				rollNo INTEGER PRIMARY KEY,  
# 				fname VARCHAR(20),  
# 				lname VARCHAR(30),  
# 				gender CHAR(1));"""

# crsr.execute(sql_command)

# crsr.execute("INSERT INTO student VALUES(01,'Ajay','Singh','M')")
# crsr.execute("INSERT INTO student VALUES(02,'Priya','Roy','F')")
# crsr.execute("INSERT INTO student VALUES(03,'Vardaan','Sethi','M')")
# crsr.execute("INSERT INTO student VALUES(04,'Rahul','Mishra','M')")


"""uPDATIION"""
conn.execute("UPDATE student SET fname = 'Riyansh' where fname='Rahul'")
conn.commit()

print("Totoal number of rows updted = " , conn.total_changes)

rows = conn.execute("SELECT * FROM student")

for row in rows:
	print(row)



"""DELETION"""
conn.execute("DELETE from student where rollNo = 04")
conn.commit()

print("TOTOAL ROWS DELTED: ", conn.total_changes)

# rows = conn.execute("SELECT * FROM student")
# for row in rows:
# 	print(row)



conn.close()
