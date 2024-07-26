import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='127.0.0.1',       
            user='root',   
            password='1v@nM1ngl3'
        )

        cursor = connection.cursor()

        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Invalid username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist")
        else:
            print(f"Error: {err}")
    else:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    create_database()
