import sqlite3
a = sqlite3.connect("company.db")
# a.execute('''create table employee(
#                         code integer,
#                         name text,
#                         designation text,
#                         salary integer,
#                         cmpname text,
#                         mobnum integer
# );''')
print("table created")
getEmplcode = input("Enter Employee code:")
getEmplname = input("Enter Employee name:")
getDesignation = input("Enter the designation of employee:")
getSalary = input("Enter the salary of employee:")
getCmpname = input("Enter Company name:")
getMobnum = input("Enter the Mobile number :")
a.execute("insert into employee(code,name,designation,salary,cmpname,mobnum)\
values("+getEmplcode+",'"+getEmplname+"','"+getDesignation+"',"+getSalary+",'"+getCmpname+"',"+getMobnum+")")
a.commit()
a.close()
print("Table inserted")