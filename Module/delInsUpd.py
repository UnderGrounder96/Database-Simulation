#!/usr/bin/python

from config import *

def delInsUpd():
	try:
		sql_query = raw_input("Please enter the entire SQL DEL/INS/UPD command: ")
		string = sql_query + ";"

		# Executes the SQL command against the database
		cursor.execute(string)

		# Commits changes in the database
		db.commit()

	except MySQLdb.Error, e:
		# Rollbacks in case there is any error
		db.rollback();

		try:
			print "MySQL Error [{}]: {}".format(e.args[0], e.args[1])

		except IndexError:
			print "MySQL Error: {}".format(str(e))

	else:
		print "The table was DEL/INS/UPD successfully."

