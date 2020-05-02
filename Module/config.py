#!/usr/bin/python

import os
import MySQLdb
from classy import MyError

try:
	os.chdir("Module/")

	# Reads from file
	with open(r"db.txt", "rb") as file:
	    d = file.readline()
	    u = file.readline()
	    p = file.readline()

	l = "localhost"
	d = d.strip()
	u = u.strip()
	p = p.strip()

	# Opens database connection
	db = MySQLdb.connect(l,u,p,d)

	# Prepares a cursor object using cursor() method
	cursor = db.cursor()

except MyError as e:
	print e

	exit(2)

