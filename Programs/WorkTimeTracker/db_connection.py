import mysql.connector
from mysql.connector import Error


def create_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='123',
            database='123'
        )
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
