import hashlib
from mysql.connector import Error
from db_connection import create_db_connection
import bcrypt


def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def register_user( email, first_name, last_name, password):
    try:
        connection = create_db_connection()
        cursor = connection.cursor()
        hashed_password = hash_password(password)
        query = "INSERT INTO users (email, first_name, last_name, password_hash) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(query, (email, first_name, last_name, hashed_password))
            connection.commit()
            print("User registered successfully")
            return True
        except Error as e:
            print(f"The error '{e}' occurred")
            return False
    except Error as e:
        print(f"The error '{e}' occurred")
        return False


def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode(), hashed_password.encode())


def login_user(email, password):
    try:
        connection = create_db_connection()
        cursor = connection.cursor()
        query = "SELECT password_hash FROM users WHERE email = %s"
        try:
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            if result and check_password(result[0], password):
                return True
            else:
                print("Login failed")
                return False
        except Error as e:
            print(f"The error '{e}' occurred")

        return False
    except Error as e:
        print(f"The error '{e}' occurred")
        return False

