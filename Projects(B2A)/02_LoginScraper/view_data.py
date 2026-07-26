from database import connect_database,get_all_data

conn,cursor =connect_database()
data =get_all_data(cursor)
for row in data:
    print(data)
conn.close()