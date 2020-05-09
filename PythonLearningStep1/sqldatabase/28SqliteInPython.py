#python sqlite

import sqlite3

#create a db file if not exits and conect wwith it
con = sqlite3.connect('employee.db')

#create cursor

c = con.cursor()

#create employee table 
"""first name, last name, pay
"""

# c.execute("""CREATE TABLE employees(
# 			first text,
# 			last text,
# 			pay integer
# 			)""")

# c.execute("INSERT INTO employees  VALUES ('Ajay', 'Siingh', 50000)")
# con.commit()
c.execute("SELECT * FROM employees WHERE last = 'Siingh'")

print(c. ())
con.commit()

con.close()