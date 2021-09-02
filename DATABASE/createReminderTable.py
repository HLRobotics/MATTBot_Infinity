import sqlite3


#Connecting to sqlite
conn = sqlite3.connect('DATABASE/MATTBOT2.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS REMINDERS")

#Creating table as per requirement
sql ='''CREATE TABLE REMINDERS(
   TOPIC CHAR(20) NOT NULL,
   TIME CHAR(20),
   DATE CHAR(20)   
)'''
cursor.execute(sql)
print("REMINDERS Table created successfully........")

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()