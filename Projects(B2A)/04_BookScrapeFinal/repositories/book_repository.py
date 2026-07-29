class BookRepository:

    def __init__(self, connection):
        self.conn = connection
        self.cursor = connection.cursor()

    def save(self, book):
        self.cursor.execute(
            '''
            INSERT INTO books(
                product_name,
                product_url,
                description,
                price,
                rating,
                availability,
                category
            )
            VALUES(?,?,?,?,?,?,?)

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

        self.conn.commit()