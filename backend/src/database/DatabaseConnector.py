import sqlite3
import os
from loguru import logger

class DatabaseConnector:
    _instance = None
    _db_path = "src/database/database.db"

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            if not os.path.exists(cls._db_path):
                raise FileNotFoundError(f"La base de datos '{cls._db_path}' no existe.")
            try:
                cls._instance = sqlite3.connect(cls._db_path)
            except sqlite3.OperationalError as e:
                print(f"Error al conectar con la base de datos: {e}")

        return cls._instance
    

    @classmethod
    def hash_database(cls):
        return os.path.exists(cls._db_path)

    @classmethod
    def make_database(cls):
        if cls.hash_database():
            return 
        
        try:
            conn = sqlite3.connect(cls._db_path)
            cursor = conn.cursor()

            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS dashboard_users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')

            conn.commit()
            conn.close()
            logger.success("Base de datos creada correctamente.")
        except sqlite3.OperationalError as e:
            print(f"Error al crear la base de datos: {e}")


        