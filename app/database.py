# database.py

import psycopg2

# Replace these values with your actual PostgreSQL database credentials
DB_NAME = "neondb"
DB_USER = "ahmobayen"
DB_PASSWORD = "85hSGYVTLHZf"
DB_HOST = "ep-green-salad-117547.eu-central-1.aws.neon.tech"
DB_PORT = "5432"


def get_db_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
