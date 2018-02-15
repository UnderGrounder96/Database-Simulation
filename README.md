Database Simulation
-------------------------
This Python program simulates a MySQL database server. By connecting with the localhost by using a root user, his password and a pre-selected database.

Getting Started
------------------
This Python program was created under Ubuntu 16.04.3 LTS Operative System, MySQL 5.7.21, Python 2.7.12, Pip 8.1.1 and MySQLdb 1.2.5.

Prerequisites
---------------
**This program uses some MySQL server configuration both in test.py and ~/Module/config.py, please change those before trying to use.

In order to use the Python program it is highly necessary to have an *internet connection* and install:
	- Pip v8.1+
	- MySQLdb v1.2+
	- Python v2.7.10+
	- MySQL v5.7.20+

i) Installing Python2
	It is possible that Python has been already installed, to check use the following code in the command line:
	
	$ python --version
	[Python 2.7.12]
	
	If errors occured or Python has not yet been installed use the following code:
	
	# refreshes the repositories
	$ sudo apt dist-upgrade
	
	# installs python
	$ sudo apt install python
	
ii) Installing MySQL v5.7.20+
	In order to install MySQL server use the following code in the command line:
	
	$ sudo apt dist-upgrade
	
	$ sudo apt install mysql-server
	
	During the installation a username and password will be requested, it is highly recommended to remember both since it is NOT possible to manage the server without them.
	As soon as MySQL server is installed it is extremely important to create a database name, using the following code in the command line:
	
	# assuming the username is root
	$ mysql -u root -p
	[enter password:] ****
	
	# after a successsful login, a "mysql>" should appear
	# assuming the desired database name is testDB
	mysql> CREATE DATABASE testDB;
	
	# after a successful database creation it is possible to exit the server
	mysql> exit

iii) Installing MySQLdb v1.2+
	In order to install MySQLdb (a MySQL module) it is necessary to install the Pip package using the following code in the command line:
	
	$ sudo apt dist-upgrade
	
	$ sudo apt install python-pip
	
	# or its variant	
	$ sudo easy_install pip
	
	# its possible to update pip using
	$ sudo pip install pip --upgrade

	After being installed it is possible to install MySQLdb itself by using the following code in the command line:
	
	# some machines require to run the following code first
	$ sudo apt build-dep python-mysqldb
	
	# installs MySQLdb
	$ sudo pip install MySQL-python
	
iv) Testing
	It is possible to pre-test the entire Python program by using the following code in the command line:

	~/Project$ python test.py
	[Database version : 5.7.21-0ubuntu0.16.04.1]

	If the output is not similar to the one above, please check the previous installation instructions. 
	In a later section of this readme should be official links for Python, MySQL, Pip and MySQLdb.

Deployment
--------------
The program was created to be easy to use and it is fool proof (to a dreggre). All user inputs return success or error messages.
In order to use please run Python file below and follow the instructions.
	~/Project$ python main.py

Files
------
/Project:
	LICENSE.md - license
	main.py - main program
	README.md - this readme
	test.py - tester
	unused - additional non-used code
	Module - folder with additional files

/Project/Module:
	altrCrtDrp.py - alters, creates and drop tables
	classy.py - MyError user-defined class
	config.py - MySQL server configuration
	delInsUpd.py - deletes from, inserts (into) and updates tables
	__int__.py - redirects package
	select.py - reads from tables
	

Versioning
------------
Version 1.6 - Current version
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
