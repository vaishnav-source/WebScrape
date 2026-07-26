import sqlite3
from config import DATABASE_NAME

def connect_database():
    conn =sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    return conn , cursor

def create_table(cursor):
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS secure_page 
        (id INTEGER PRIMARY KEY AUTOINCREMENT ,
        heading TEXT,
        message TEXT,
        scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
         )
    ''')

def insert_data(cursor,data):
    cursor.execute('''
                   INSERT INTO secure_page (heading,message)
                   VALUES(?,?)
                   ''',(
                   data["heading"],
                   data["message"]
                   )
    )

def get_all_data(cursor):
    cursor.execute('SELECT * FROM secure_page')
    return cursor.fetchall()

