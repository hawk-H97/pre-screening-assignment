import os
import time#
import psycopg2
from psycopg2 import OperationalError

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection(retries=5, delay=2):
    for attempt in range (retries):
        try:
            return psycopg2.connect(DATABASE_URL)
        except OperationalError as e:
            print(f"Database connection failed (attempt {attempt + 1}/{retries})")
            print(str(e))
            time.sleep(delay)
    raise Exception("Could not connect to the database after serveral retries.")