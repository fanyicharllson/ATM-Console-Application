import sqlite3
import logging

file_handler = logging.FileHandler("Database.log")
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s', handlers=[file_handler])

def Database(db_path: str):
    try:
        connection = sqlite3.connect(db_path);
        logging.info(f"Database connected successfully at {db_path}")
        return connection
        
    except sqlite3.Error as e:
            logging.error(f"Error connecting to database: {db_path}")
            return None         