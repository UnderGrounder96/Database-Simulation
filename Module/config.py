#!/usr/bin/python

import MySQLdb

root = "root"
dbName = "testDB"
password = "1234"
localhost = "localhost"

# Opens database connection
db = MySQLdb.connect(localhost, root, password, dbName)

# Prepares a cursor object using cursor() method
cursor = db.cursor()