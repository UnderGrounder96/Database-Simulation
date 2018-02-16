#!/usr/bin/python

import os
import MySQLdb
from classy import MyError

try:
	os.chdir("Module/")

	# Reads from file
	fi = open(r"db.txt", "rb")	
	u = fi.readline()
	p = fi.readline()
	d = fi.readline()
	l = "localhost"	

	# Closes read file
	fi.close()

	u = u.strip()
	p = p.strip()
	d = d.strip()		

	# Opens database connection
	db = MySQLdb.connect(l,u,p,d)

	# Prepares a cursor object using cursor() method
	cursor = db.cursor()

except MyError as e:
	print e

else:
	pass