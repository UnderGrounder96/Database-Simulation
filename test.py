#!/usr/bin/python
#Lucio Afonso

import getpass
import argparse
import MySQLdb

#MyError class
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
	parser = argparse.ArgumentParser(description="This the pre-test of the program. \
Please run \'python test.py\' and follow the instructions to complete the pre-test.")
	parser.parse_args()

	print "This programs assumes that the database is connected via localhost\n"

	d = raw_input("Please insert the database name: ")
	u = raw_input("Please insert the database username: ")
	p = getpass.getpass(prompt="Please insert the database password: ")

	# Creates a file
	fo = open(r"Module/db.txt", "wb")
	fo.write(r""+d+"\n");
	fo.write(r""+u+"\n");
	fo.write(r""+p);

	# Opens database connection
	db = MySQLdb.connect("localhost",u,p,d)

	# Prepares a cursor object using cursor() method
	cursor = db.cursor()

	# Executes SQL query using execute() method.
	cursor.execute("SELECT VERSION()")

	# Fetchs a single row using fetchone() method.
	data = cursor.fetchone()

	print "\nDatabase version : %s " % data

except MySQLdb.Error as e:
	print "\nIt wasn\'t possible to connect with the database. \
Please verify if the correct username, password and database name were used.\nFull MySQL error: ", e
	exit(1)

except MyError as e:
	print e
	exit(2)

else:
	print "\nCongratulations! The connection was established.\nYou're now able to run \'python main.py\'."

	# Closes opened file
	fo.close()

	# Closes all cursors
	cursor.close()

	# Disconnects from server
	db.close()

	exit(0)
