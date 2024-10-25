import mysql.connector
from mysql.connector import Error


def create_database():
    my_db = None
    my_cursor = None
    try:
        # Establish a connection to the MySQL server
        my_db = mysql.connector.connect(
            host="localhost",
            user="",
            password=""
            
        )

        if my_db.is_connected():
            my_cursor = my_db.cursor()

            # Creating database
            my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f'Error: {e}')

    finally:
        # Ensure that the cursor and database connection are closed properly
        if my_cursor:
            my_cursor.close()

        if my_db and my_db.is_connected():
            my_db.close()
