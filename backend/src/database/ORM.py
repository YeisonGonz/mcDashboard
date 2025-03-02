import sqlite3
from loguru import logger
import hashlib


class ORM:

    def __init__(self, connector):
        self.connector = connector

    def _hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()
    def num_dashboardUsers(self):
        cursor = self.connector.cursor()
        cursor.execute("SELECT COUNT(*) FROM dashboard_users")
        count = cursor.fetchone()[0]
        return count
    
    def insert_dashboardUser(self, name, password):

        try:
            cursor = self.connector.cursor()
            query = "INSERT INTO dashboard_users (name, password) VALUES (?, ?)"
            cursor.execute(query, (name, password))
            self.connector.commit()  
            logger.debug(f"User {name} insert succesfully")
            return cursor.lastrowid 
        except sqlite3.IntegrityError as e:
            logger.error(e) 
            return False
        
    def verify_password(self, name, password):
        cursor = self.connector.cursor()
        query = "SELECT password FROM dashboard_users WHERE name = ?"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        
        if result:
            stored_password = result[0]
            hashed_input_password = self._hash_password(password)
            return stored_password == hashed_input_password
        return False
