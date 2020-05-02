#!/usr/bin/python
#Lucio Afonso

import getpass
import argparse
import MySQLdb

try:
	parser = argparse.ArgumentParser(description="This the pre-test of the \
program. Please run \'python test.py\' and follow the instructions to complete \
the pre-test.")

	parser.parse_args()

	print "This programs assumes that the database is connected via localhost\n"

	d = raw_input("Please insert the database name: ")
	u = raw_input("Please insert the database username: ")
	p = getpass.getpass(prompt="Please insert the database password: ")

	# Creates a file
	with open(r"Module/db.txt", "wb") as file:
		file.write(r""+d+"\n");
		file.write(r""+u+"\n");
		file.write(r""+p);

	# Opens database connection
	db = MySQLdb.connect("localhost",u,p,d)

	# Prepares a cursor object using cursor() method
	cursor = db.cursor()

	# Executes SQL query using execute() method.
	cursor.execute("SELECT VERSION()")

	# Fetchs a single row using fetchone() method.
	data = cursor.fetchone()

	print '\n'
	print "Database version : {} ".format(data)

except MySQLdb.Error as e:
	print '\n'

	print "It wasn\'t possible to connect with the database. \
Please verify if the correct username, password and database name were used.\n \
Full MySQL error: "

	print e

	exit(1)

else:
	print "\nCongratulations! The connection was established.\nYou're now able \
to run \'python main.py\'."

	# Closes all cursors
	cursor.close()

	# Disconnects from server
	db.close()

	exit(0)

