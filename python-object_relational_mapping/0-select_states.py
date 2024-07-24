#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

def list_states(username, password, db_name):
    """
    Lists all states from the database hbtn_0e_0_usa.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        db_name (str): The database name.
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query to select all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Get MySQL username, password, and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # List all states
    list_states(mysql_username, mysql_password, db_name)