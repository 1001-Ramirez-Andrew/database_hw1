# database_hw1

Database Design:
The Datbase is designed with directory and file implementation. In this implementaiton, Databases are Directories that exist in the same directory as the main.py program.
Tables are implemented as files that exist inside their corresponding Database directories. The varaible and variable types for a table are stored as an n-tuple string in the first line of the file.
Database and Table names in the file system are exactly as users eneter them in the program. Multiple Databases(directories) exist inside the directory that the main.py program is run. Multiple Tables(files) exist inside the their Databse Directory. 

How to Run:
If in the directory of main.py you can use inderection to run the list of commadns as follows:
python3 main.py < PA1_test.sql

This will give the list of requried outputs. Notice that the first line is not a command because it is a comment in the .sql file.

IMPORTANT!: This will only compile on Python3.9 and greater because some string methods used are non-existant in older versions of python. 

