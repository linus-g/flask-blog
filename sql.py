# sql.py - Create a SQLite3 table and populate it with data

import sqlite3
from sqlite3.dbapi2 import connect

# create a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:
    
    # get a cursor object used to execute SQL commands
    cursor = connection.cursor()

    # create the table
    cursor.execute("""CREATE TABLE posts (title TEXT, post TEXT)""")

    # insert dummy data into the table
    cursor.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    cursor.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    cursor.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    cursor.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
