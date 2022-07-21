#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         USERNAME       TEXT    NOT NULL,
         FIRSTNAME      TEXT    NOT NULL,
         LASTNAME       TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
         
print("Table created successfully")

conn.execute("INSERT OR IGNORE INTO COMPANY (ID,USERNAME,FIRSTNAME,LASTNAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'paulinator', 'Paul', 'Nate', 32, 'California', 20000.00 )");

conn.execute("INSERT OR IGNORE INTO COMPANY (ID,USERNAME,FIRSTNAME,LASTNAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'asmith', 'Allen', 'Smith', 25, 'Texas', 15000.00 )");

conn.execute("INSERT OR IGNORE INTO COMPANY (ID,USERNAME,FIRSTNAME,LASTNAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'tbear', 'Teddy', 'Bear', 23, 'Norway', 20000.00 )");

conn.execute("INSERT OR IGNORE INTO COMPANY (ID,USERNAME,FIRSTNAME,LASTNAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'thehulk', 'Mark', 'Ruffalo', 25, 'Rich-Mond ', 65000.00 )");
      
conn.execute("INSERT OR IGNORE INTO COMPANY (ID,USERNAME,FIRSTNAME,LASTNAME,AGE,ADDRESS,SALARY) \
      VALUES (5, 'joe', 'Joe', 'Bloggs', 35, 'Scotsdale ', 25000.00 )");
      
print("Populated database successfully")