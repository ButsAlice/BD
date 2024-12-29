import psycopg2

class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='admin',
            host='localhost',
            port=5432
        )
        self.create_tables()

    def create_tables(self):
        c = self.conn.cursor()
        # Check for tables
        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'performance')")
        performance_table_exists = c.fetchone()[0]

        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'festival')")
        festival_table_exists = c.fetchone()[0]

        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'artist')")
        artist_table_exists = c.fetchone()[0]

        if not performance_table_exists:
            c.execute('''
                        CREATE TABLE performance (
                            performance_id SERIAL PRIMARY KEY,
                            festival_id INTEGER NOT NULL,
                            artist_id INTEGER NOT NULL,
                            start_time TIME,
                            finish_time TIME
                        )
                    ''')
        if not festival_table_exists:
            c.execute('''
                        CREATE TABLE "festival" (
                            "festival_id" SERIAL PRIMARY KEY,
                            "fest_name" TEXT NOT NULL,
                            "fest_date" DATE NOT NULL,
                            "fest_place" TEXT NOT NULL
                        )
                    ''')
        if not artist_table_exists:
            c.execute('''
                        CREATE TABLE "artist" (
                            "artist_id" SERIAL PRIMARY KEY,
                            "artist_name" TEXT NOT NULL,
                            "artist_genre" TEXT
                        )
                    ''')

        self.conn.commit()