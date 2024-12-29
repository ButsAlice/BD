class ModelFestival:
    def __init__(self, db_model):
        self.conn = db_model.conn

    def add_Festival(self, Festival_ID, Fest_name, Price, City):
        c = self.conn.cursor()
        try:
            c.execute('INSERT INTO "Festival" ("Festival_ID", "Fest_name", "Price", "City") VALUES (%s, %s, %s, %s)',
                      (Festival_ID, Fest_name, Price, City))
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Adding A Festival: {str(e)}")
            return False  # Returns False if insertion fails

    def get_all_Festivals(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Festival"')
        return c.fetchall()

    def update_Festival(self, Festival_ID, Fest_name, Price, City):
        c = self.conn.cursor()
        try:
            c.execute('UPDATE "Festival" SET "Fest_name"=%s, "Price"=%s, "City"=%s WHERE "Festival_ID"=%s',
                      (Fest_name, Price, City, Festival_ID))
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Updating A Festival: {str(e)}")
            return False   # Returns False if insertion fails

    def delete_Festival(self, Festival_ID):
        c = self.conn.cursor()
        try:
            c.execute('DELETE FROM "Festival" WHERE "Festival_ID"=%s', (Festival_ID,))
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Deleting A Festival Violates A Foreign Key Constraint: {str(e)}")
            return False   # Returns False if insertion fails

    def check_Festival_existence(self, Festival_ID):
        c = self.conn.cursor()
        c.execute('SELECT 1 FROM "Festival" WHERE "Festival_ID" = %s', (Festival_ID,))
        return bool(c.fetchone())

    def create_Festival_sequence(self):
        # Check for the existence of a sequence
        c = self.conn.cursor()
        c.execute("""
        DO $$
           BEGIN
               IF NOT EXISTS (SELECT 1 FROM pg_sequences WHERE schemaname = 'public' AND sequencename = 'festival_id_seq') THEN
                   CREATE SEQUENCE festival_id_seq;
               ELSE
                   DROP SEQUENCE festival_id_seq;
                   CREATE SEQUENCE festival_id_seq;
               END IF;
           END $$;
        """)
        self.conn.commit()

    def generate_rand_Festival_data(self, number_of_operations):
        c = self.conn.cursor()
        try:
            # Insert data
            c.execute("""
            INSERT INTO "Festival" ("Festival_ID", "Fest_name", "Price", "City")
            SELECT
                nextval('festival_id_seq'), 
                (array['Fire', 'Dance', 'Loud', 'Music', 'Instrumental', 'Box'])[floor(random() * 6) + 1], 
                random() * 1000 ,
                (array['London', 'Lviv', 'Paris', 'Berlin', 'Stockholm'])[floor(random() * 5) + 1]  
            FROM generate_series(1, %s);
            """, (number_of_operations,))
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Adding The Festivals: {str(e)}")
            return False   # Returns False if insertion fails


    def truncate_Festival_table(self):
        c = self.conn.cursor()
        try:
            # Insert data
            c.execute("""DELETE FROM "Festival" """)
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Deleting All Festival`s Data: {str(e)}")
            return False   # Returns False if insertion fails