#!/usr/bin/python
#Lucio Afonso gr. 1

import MySQLdb

# Opens database connection
db = MySQLdb.connect("localhost","root","1234","testDB")

# Prepares a cursor object using cursor() method
cursor = db.cursor()

# Executes SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetchs a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# Closes all cursors
cursor.close()

# Disconnects from server
db.close()