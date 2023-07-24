import logging
import sqlite3

database = 'pfsuc_database.db'
base_path = r"C:\Users\outri\opensource\python-flask-sqlite3-users-crud"


class DBConnection:
    def __init__(self):
        self.db_conn = sqlite3.connect(base_path + "/" + database, check_same_thread=False)
        self.cursor = self.db_conn.cursor()

    def create_tables(self):
        logging.info(f"Method to create tables if table not exists")
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, age INTEGER, status BOOLEAN)")
            self.db_conn.commit()
            return True, None, "Table created successfully", 201
        except Exception as error:
            logging.exception(f"unable to connect to db with error {error}")
            return False, None, f"Failed create database with error {error}", 500

    def create_user(self, user):
        logging.info("Method to create user record")
        try:
            self.cursor.execute('INSERT INTO users (name, email, age, status) VALUES (?, ?, ?, ?)', (user.name, user.email, user.age, user.status))
            self.db_conn.commit()
            self.db_conn.close()
            return True, user.__dict__, "User created successfully", 201
        except Exception as error:
            logging.exception(f"Failed to create user data with error {error}")
            return False, None, f"Failed to create user data with error {error}", 500

    def get_users(self):
        logging.info("Method to get users records")
        try:
            self.cursor.execute('SELECT * FROM users')
            users = self.cursor.fetchall()
            self.db_conn.close()
            if users:
                return True, users, "User details fetched successfully", 200
            return False, None, f"No users found", 200
        except Exception as error:
            logging.exception(f"Failed to get users data with error {error}")
            return False, None, f"Failed to get users data with error {error}", 500

    def get_user(self, user_id):
        logging.info("Method to get user record")
        try:
            self.cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            user = self.cursor.fetchone()
            self.db_conn.close()
            if user:
                return True, user, "User details fetched successfully", 200
            return False, None, f"user not found", 200
        except Exception as error:
            logging.exception(f"Failed to get user data with error {error}")
            return False, None, f"Failed to get user data with error {error}", 500

    def update_user(self, user_id, new_user):
        logging.info("Method to update user record")
        try:
            self.cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            user = self.cursor.fetchone()
            if not user:
                return False, None, 'User not found', 200
            self.cursor.execute('UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?', (
                new_user.name, new_user.email, new_user.age, user_id))
            self.db_conn.commit()
            self.db_conn.close()
            return True, new_user.__dict__, "User details updated successfully", 200
        except Exception as error:
            logging.exception(f"Failed to update user data with error {error}")
            return False, None, f"Failed to update user data with error {error}", 500

    def delete_user(self, user_id):
        logging.info("Method to delete user record")
        try:
            self.cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            user = self.cursor.fetchone()
            if not user:
                return False, None, 'User not found', 200
            self.cursor.execute('UPDATE users SET status = ? WHERE id = ?', (
                False, user_id))
            self.db_conn.commit()
            self.db_conn.close()
            return True, {"user_id": user_id}, "User deleted successfully", 200
        except Exception as error:
            logging.exception(f"Failed to delete user data with error {error}")
            return False, None, f"Failed to delete user data with error {error}", 500
