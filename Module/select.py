#!/usr/bin/python

from config import *

def select():
	try:
		sql = raw_input("Please enter the entire SQL SELECT command: ")
		string = sql+";"

		# Executes the SQL command against the database	
		cursor.execute(string)

		# Fetchs all the rows in a list of lists.
		results = cursor.fetchall()

		#count = cursor.rowcount

		for row in results:
			for col in row:
				print "%s," % col
			print "\n"

	except:
		print "Error: unable to fecth data, please verify the input.\n"

	else:
		print "The data was SELECTED successfully.\n"
