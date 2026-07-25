import sqlite3

def connect_database():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            stock TEXT NOT NULL,
            price REAL NOT NULL,
            rating REAL NOT NULL
        )
    ''')

def insert_book(cursor,book):
    cursor.execute(''' 
                INSERT OR IGNORE INTO books(title,stock,price,rating) VALUES(?,?,?,?)''', 
                    (   book["title"],
                        book["stock"],
                        book["price"],
                        book["rating"] 
                    ) 
        )
    

def get_all_books(cursor):
    cursor.execute('SELECT * FROM books')
    return cursor.fetchall()


def close_connection(conn):
    conn.commit()
    conn.close()