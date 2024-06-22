import sqlite3

# connect to sqlite
connection=sqlite3.connect("student.db") 

# create a cursor object to insert record, create table, retrieve
cursor=connection.cursor()

#create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""
cursor.execute(table_info)

# insert some records
cursor.execute('''insert into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''insert into STUDENT values('Subh','Data Science','B',100)''')
cursor.execute('''insert into STUDENT values('Darius','Data Science','A',86)''')
cursor.execute('''insert into STUDENT values('Vikash','DEVOPS','A',50)''')
cursor.execute('''insert into STUDENT values('Dipesh','DEVOPS','A',35)''')

#display all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

#close the connection

connection.commit()
connection.close()