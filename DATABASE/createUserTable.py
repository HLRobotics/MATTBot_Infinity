import sqlite3


#Connecting to sqlite
conn = sqlite3.connect('DATABASE/MATTBOT2.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS USER")

#Creating table as per requirement
sql ='''CREATE TABLE USER(
   NAME CHAR(20) NOT NULL,
   MAIL CHAR(20),
   OS CHAR(20),
   VOCAL_STATUS CHAR(20)
)'''
cursor.execute(sql)
print("USER Table created successfully........")

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()