import psycopg2

class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='qwerty',
            host='localhost',
            port=5432
        )
        self.create_tables()

    def create_tables(self):
        c = self.conn.cursor()
        # Check for tables
        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'Perfomance')")
        Performance_table_exists = c.fetchone()[0]

        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'Festival')")
        Festival_table_exists = c.fetchone()[0]

        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'Performer')")
        Performer_table_exists = c.fetchone()[0]

        if not Performance_table_exists:
            c.execute('''
                        CREATE TABLE Perfomance (
                            Preformance_ID SERIAL PRIMARY KEY,
                            Festival_ID INTEGER NOT NULL,
                            Artist_ID INTEGER NOT NULL,
                            Start_time DATE NOT NULL,
                            Finish_time DATE NOT NULL
                        )
                    ''')
        if not Festival_table_exists:
            c.execute('''
                        CREATE TABLE "Festival" (
                            "Festival_ID" SERIAL PRIMARY KEY,
                            "Fest_name" TEXT NOT NULL,
                            "Price" INTEGER NOT NULL,
                            "City" TEXT NOT NULL
                        )
                    ''')
        if not Performer_table_exists:
            c.execute('''
                        CREATE TABLE "Performer" (
                            "Artist_ID" SERIAL PRIMARY KEY,
                            "name" TEXT NOT NULL
                            "surname" TEXT NOT NULL
                            "genre" TEXT
                        )
                    ''')

        self.conn.commit()