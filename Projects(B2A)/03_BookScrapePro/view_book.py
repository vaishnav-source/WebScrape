from  database import connect_database,get_all_books

conn,cursor =connect_database()
books =get_all_books(cursor)
for book in books:
    print(book)
