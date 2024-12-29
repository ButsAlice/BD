class ModelPerformer:
    def __init__(self, db_model):
        self.conn = db_model.conn

    def add_Performer(self, Artist_ID, name, surname, genre):
        c = self.conn.cursor()
        try:
            c.execute('INSERT INTO "Performer" ("Artist_ID" ,"name", "surname", "genre") VALUES (%s, %s, %s, %s)', (Artist_ID, name, surname, genre))
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Adding A Performer: {str(e)}")
            return False   # Returns False if insertion fails

    def get_all_Performers(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Performer"')
        return c.fetchall()

    def update_Performer(self, Artist_ID, name, surname, genre):
        c = self.conn.cursor()
        try:
            c.execute('UPDATE "Performer" SET "name"=%s, "surname"=%s, "genre"=%s WHERE "Artist_ID"=%s', (name, surname, genre, Artist_ID))
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With A Performer Updating: {str(e)}")
            return False   # Returns False if insertion fails

    def delete_Performer(self, Artist_ID):
        c = self.conn.cursor()
        try:
            c.execute('DELETE FROM "Performer" WHERE "Artist_ID"=%s', (Artist_ID,))
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With An Artist Deleting: {str(e)}")
            return False  # Returns False if insertion fails

    def check_Performer_existence(self, Artist_ID):
        c = self.conn.cursor()
        c.execute('SELECT 1 FROM "Performer" WHERE "Artist_ID" = %s', (Artist_ID,))
        return c.fetchone() is not None

    def create_Performer_sequence(self):
        # Check for the existence of a sequence
        c = self.conn.cursor()
        c.execute("""
            DO $$
           BEGIN
               IF NOT EXISTS (SELECT 1 FROM pg_sequences WHERE schemaname = 'public' AND sequencename = 'artist_id_seq') THEN
                   CREATE SEQUENCE artist_id_seq;
               ELSE
                   DROP SEQUENCE artist_id_seq;
                   CREATE SEQUENCE artist_id_seq;
               END IF;
           END $$;
        """)
        self.conn.commit()
    def generate_rand_Performer_data(self, number_of_operations):
        c = self.conn.cursor()
        try:
            # Insert data
            c.execute("""
            INSERT INTO "Performer" ("Artist_ID" ,"name", "surname", "genre")
            SELECT
                nextval('artist_id_seq'), 
                (array['Ivan', 'Mike', 'John', 'Harry'])[floor(random() * 4) + 1],
                (array['Lenon', 'Muller', 'Vachovski', 'Potter'])[floor(random() * 4) + 1],
                (array['Rock', 'Jazz', 'All', 'Pop'])[floor(random() * 4) + 1]     
            FROM generate_series(1, %s);
            """, (number_of_operations,))
            self.conn.commit()
            return True  # Returns True if the insertion was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With A Performer Adding: {str(e)}")
            return False   # Returns False if insertion fails

    def truncate_Performer_table(self):
        c = self.conn.cursor()
        try:
            # Insert data
            c.execute("""DELETE FROM "Performer" """)
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With A Performer`s Data Deleting: {str(e)}")
            return False   # Returns False if insertion fails