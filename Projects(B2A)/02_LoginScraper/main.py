from auth import login
from scraper import scrape_secure_page
from database import connect_database, create_table,insert_data

conn , cursor =connect_database()
try:
    create_table(cursor)
    session = login()
    data = scrape_secure_page(session)
    insert_data(cursor,data)
    conn.commit()
except Exception as error:
    print(f"Program failed: {error}")
    conn.rollback()
finally:
    conn.close()


