#!/usr/bin/python

from .config import *

def altrCrtDrp():
	try:
		sql_query = input("Please enter the entire SQL ALT/CRT/DRP TABLE command: ")

		string = sql_query + ";"

		# Executes the SQL command against the database
		cursor.execute(string)

	except MySQLdb.Error as e:
		try:
			print("MySQL Error [{}]: {}".format(e.args[0], e.args[1]))

		except IndexError:
			print("MySQL Error: {}".format(str(e)))

	else:
		print("The table was ALT/CRT/DRP successfully.\n")
