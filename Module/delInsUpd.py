#!/usr/bin/python

from config import *

def delInsUpd():
	try:
		
		sql = raw_input("Please enter the entire SQL DEL/INS/UPD command: ")
		string = sql+";"
		
		# Executes the SQL command against the database	
		cursor.execute(string)
		
		# Commits changes in the database
		db.commit()


	except MySQLdb.Error, e:
		# Rollbacks in case there is any error
		db.rollback();
		try:
			print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
		except IndexError:
			print "MySQL Error: %s" % str(e)
	
	else:
		print "The table was DEL/INS/UPD successfully."