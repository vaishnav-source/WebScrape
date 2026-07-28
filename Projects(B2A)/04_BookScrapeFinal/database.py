import sqlite3
from config import DATABASE_NAME


def connect_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    return conn ,cursor

def create_table(cursor):
    cursor.execute('''
CREATE TABLE IF NOT EXISTS books(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   product_name TEXT NOT NULL,
                   product_url TEXT NOT NULL UNIQUE,
                   description TEXT NOT NULL,
                   price REAL NOT NULL,
                   rating INTEGER NOT NULL,
                   availability TEXT NOT NULL,
                   category TEXT NOT NULL,
                   last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')


def upsert_book(cursor,book):
    cursor.execute('''INSERT  INTO books(product_name,product_url,description,price,
                   rating,availability,category) VALUES(?,?,?,?,?,?,?)
                    ON CONFLICT(product_url) DO UPDATE SET
                    price = excluded.price,
            rating = excluded.rating,
            availability = excluded.availability,
            last_updated = CURRENT_TIMESTAMP

        WHERE
            books.price != excluded.price
            OR books.rating != excluded.rating
            OR books.availability != excluded.availability
        ''',
        (
            book["product_name"],
            book["product_url"],
            book["description"],
            book["price"],
            book["rating"],
            book["availability"],
            book["category"]
        )
    )

def get_all_books(cursor):
    cursor.execute ('SELECT * FROM books')
    return cursor.fetchall()
