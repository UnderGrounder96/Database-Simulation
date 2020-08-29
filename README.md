## Database-Simulation

This Python program simulates a MySQL database server.

## Getting Started

This Python program was created under Ubuntu 16.04.3 LTS Operative System,<br />
MySQL 5.7.21, Python 3.8.2, Pip 8.1.1 and MySQLdb 1.2.5.

## Prerequisites

\*MySQL in some machines may require sudo.<br />
\*\*After installing, it is very important to run the **test.py**, before first use.

i) Installing Python v3.8.2+
It is possible that Python has been already installed, one could check by using the commands:

    $ python3 --version
    [Python 3.8.2]

    If errors occurred or Python has not yet been installed use the following code:

    $ sudo apt dist-upgrade
    # refreshes the repositories

    $ sudo apt install python3
    # installs python3

ii) Installing MySQL v5.7.20+
It is possible that MySQL has been already installed, one could check by using the commands:

    $ sudo mysql --version
    [mysql  Ver 14.14 Distrib 5.7.24]

    To ensure a secure (and easiest possible) install,
    please refer to this website *last visited - 02/May/2020*:

    https://support.rackspace.com/how-to/installing-mysql-server-on-ubuntu/

iii) Installing MySQLdb v1.2+
In order to install MySQLdb (a MySQL module) and PIP, one could check by using the commands:

    $ python3 -m pip --version
    [pip 20.2.2 from ... (python 3.8)]

    # or its variant
    $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $ python3 get-pip.py

    # its possible to update pip using
    $ python3 -m pip install -U pip

    After installing pip it is possible to install MySQLdb itself
    by using the following commands:

    # some machines require to run the following code first
    $ sudo apt build-dep python-mysqldb

    # installs MySQLdb
    $ sudo apt install python3-dev libmysqlclient-dev
    $ pip install -r requirements.txt

iv) Testing
Importing the default file to your MySQL server, It would be possible to pre-test the entire Python program by
using the following code in the command line:

    # database: app; table: users
    # sudo mysql -u root -p < db.sql

    ~/Database-Simulation$ sudo python test.py
    [This programs assumes that the database is connected via localhost]
    [Database version : 5.7.21-0ubuntu0.16.04.1]
    [Congratulations! The connection was established.]

    If the output is not similar to the one above,
    please check the previous installation instructions.

## Deployment

The program was created to be easy to use and it is fool proof (to a degree).<br />
All user inputs return success or error messages.<br />
In order to use please run Python file below and follow the instructions.

    ~/Database-Simulation$ sudo python main.py

## Files

/Database-Simulation:<br />
LICENSE.md - license<br />
main.py - main program<br />
README.md - this readme<br />
test.py - tester<br />
unused - additional non-used code<br />
Module - folder with additional files<br />
db.sql - dummy SQL database<br />

/Database-Simulation/Module:<br />
altrCrtDrp.py - alters, creates and drop tables<br />
classy.py - MyError user-defined class<br />
config.py - MySQL server configuration<br />
delInsUpd.py - deletes from, inserts (into) and updates tables<br />
**int**.py - redirects package<br />
select.py - reads from tables<br />
db.txt - read-only, created after running test.py \*<br />

## Versioning

Version 1.9 - Current version<br />
Version 2.0(TBA) - GUI support

## Author

Lucio Afonso

## License

This project is licensed under the GPL License - see the LICENSE.md file for details

## Acknowledgments

Official sites:

https://www.python.org/<br />
https://www.mysql.com/<br />
https://github.com/pypa/pip<br />

Tutorials:

https://www.w3schools.com/sql/<br />
http://mysqlclient.readthedocs.io/<br />
https://www.tutorialspoint.com/python/<br />
http://www.mikusa.com/python-mysql-docs/index.html<br />
