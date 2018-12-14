#!/usr/bin/python

from config import *

def altrCrtDrp():
	try:
		sql = raw_input("Please enter the entire SQL ALT/CRT/DRP TABLE command: ")
		string = sql+";"

		# Executes the SQL command against the database
		cursor.execute(string)

	except MySQLdb.Error, e:
		try:
			print "MySQL Error [%d]: %s\n" % (e.args[0], e.args[1])
		except IndexError:
			print "MySQL Error: %s\n" % str(e)

	else:
		print "The table was ALT/CRT/DRP successfully.\n"
