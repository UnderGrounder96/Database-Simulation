#!/usr/bin/python

from .config import *

def select():
	try:
		sql_query = input("Please enter the entire SQL SELECT command: ")

		string = sql_query + ";"

		# Executes the SQL command against the database
		cursor.execute(string)

		# Fetch all the rows in a list of lists.
		results = cursor.fetchall()

		#count = cursor.rowcount

		for row in results:
			for col in row:
				print("%s," % col)

			print()

	except:
		print("Error: unable to fetch data, please verify the input.\n")

	else:
		print("The data was SELECTED successfully.\n")
