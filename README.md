Database-Simulation
-------------------------
This Python program simulates a MySQL database server. By connecting with the localhost and using a root user, his password and a pre-selected database.

Getting Started
------------------
This Python program was created under Ubuntu 16.04.3 LTS Operative System, MySQL 5.7.21, Python 2.7.12, Pip 8.1.1 and MySQLdb 1.2.5.

Prerequisites
---------------
**After installing, it is very important to fully test the program using the test.py, before first use.

In order to use the Python program it is highly necessary to have an *internet connection* and install:
	- Pip v8.1+
	- MySQLdb v1.2+
	- Python v2.7.10+
	- MySQL v5.7.20+

i) Installing Python v2.7.10+
	It is possible that Python has been already installed, to check use the following code in the command line:

	$ python --version
	[Python 2.7.12]

	If errors occured or Python has not yet been installed use the following code:

	$ sudo apt dist-upgrade
	# refreshes the repositories

	$ sudo apt install python
	# installs python

ii) Installing MySQL v5.7.20+
	It is possible that Python has been already installed, to check use the following code in the command line:

	$ mysql --version
	[mysql  Ver 14.14 Distrib 5.7.24]

	To ensure a secure (and easiest possible) install,
	please refer to this website *last visited - 14/Dec/2018*:

	https://support.rackspace.com/how-to/installing-mysql-server-on-ubuntu/

iii) Installing MySQLdb v1.2+
	In order to install MySQLdb (a MySQL module) it is necessary to install the Pip package
	using the following code in the command line:

	$ sudo apt dist-upgrade

	$ sudo apt install python-pip

	# or its variant
	$ sudo easy_install pip

	# its possible to update pip using
	$ sudo pip install pip --upgrade

	After being installed it is possible to install MySQLdb itself
	by using the following code in the command line:

	# some machines require to run the following code first
	$ sudo apt build-dep python-mysqldb

	# installs MySQLdb
	$ sudo apt-get install python-dev libmysqlclient-dev
	$ python -m pip install --user MySQL-python

iv) Testing
	Importing the default file to your MySQL server, It would be possible to pre-test the entire Python program by
	using the following code in the command line:
	
	# database: app; table: users
	# sudo mysql -u root -p &lt db sql
	
	~/Project$ python test.py
	[This programs assumes that the database is connected via localhost]
	[Database version : 5.7.21-0ubuntu0.16.04.1]
	[Congratulations! The connection was established.]

	If the output is not similar to the one above,
	please check the previous installation instructions.

Deployment
--------------
The program was created to be easy to use and it is fool proof (to a dreggre). All user inputs return success or error messages.
In order to use please run Python file below and follow the instructions.

	~/Database-Simulation$ python main.py

Files
------
/Database-Simulation:
	LICENSE.md - license
	main.py - main program
	README.md - this readme
	test.py - tester
	unused - additional non-used code
	Module - folder with additional files
	db.sql - dummy SQL database

/Database-Simulation/Module:
	altrCrtDrp.py - alters, creates and drop tables
	classy.py - MyError user-defined class
	config.py - MySQL server configuration
	delInsUpd.py - deletes from, inserts (into) and updates tables
	__int__.py - redirects package
	select.py - reads from tables

Versioning
------------
Version 1.8 - Current version

Version 2.0(TBA) - GUI support

Author
---------
Lucio Afonso

License
---------
This project is licensed under the GPL License - see the LICENSE.md file for details

Acknowledgments
----------------------
Official sites:

	https://www.python.org/
	https://www.mysql.com/
	https://github.com/pypa/pip

Tutorials:

	https://www.w3schools.com/sql/
	http://mysqlclient.readthedocs.io/
	https://www.tutorialspoint.com/python/
	http://www.mikusa.com/python-mysql-docs/index.html
