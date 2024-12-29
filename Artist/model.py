class ModelArtist:
    def __init__(self, db_model):
        self.conn = db_model.conn

    def add_artist(self, artist_id, artist_name, artist_genre):
        c = self.conn.cursor()
        try:
            c.execute('INSERT INTO "artist" ("artist_id" ,"artist_name", "artist_genre") VALUES (%s, %s, %s)', (artist_id, artist_name, artist_genre))
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Adding An Artist: {str(e)}")
            return False   # Returns False if insertion fails

    def get_all_artists(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "artist"')
        return c.fetchall()

    def update_artist(self, artist_id, artist_name, artist_genre):
        c = self.conn.cursor()
        try:
            c.execute('UPDATE "artist" SET "artist_name" = %s, "artist_genre" = %s WHERE "artist_id" = %s', (artist_name, artist_genre, artist_id))
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With An Artist Updating: {str(e)}")
            return False   # Returns False if insertion fails

    def delete_artist(self, artist_id):
        c = self.conn.cursor()
        try:
            c.execute('DELETE FROM "artist" WHERE "artist_id"=%s', (artist_id,))
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With An Artist Deleting: {str(e)}")
            return False  # Returns False if insertion fails

    def check_artist_existence(self, artist_id):
        c = self.conn.cursor()
        c.execute('SELECT 1 FROM "artist" WHERE "artist_id" = %s', (artist_id,))
        return c.fetchone() is not None

    def create_artist_sequence(self):
        # Check for the existence of a sequence and ensure it starts with the correct value
        c = self.conn.cursor()
        c.execute("""
            DO $$
            DECLARE
                max_id INT;
            BEGIN
                -- Find the maximum existing artist_id
                SELECT COALESCE(MAX(artist_id), 0) INTO max_id FROM artist;

                -- Check if the sequence exists
                IF NOT EXISTS (
                    SELECT 1 
                    FROM pg_sequences 
                    WHERE schemaname = 'public' AND sequencename = 'artist_id_seq'
                ) THEN
                    -- Create a new sequence starting after the max_id
                    EXECUTE 'CREATE SEQUENCE artist_id_seq START WITH ' || (max_id + 1);
                ELSE
                    -- Reset the existing sequence to start after the max_id
                    EXECUTE 'ALTER SEQUENCE artist_id_seq RESTART WITH ' || (max_id + 1);
                END IF;
            END $$;
        """)
        self.conn.commit()

    def generate_rand_artist_data(self, number_of_operations):
        c = self.conn.cursor()
        try:
            # Insert data
            c.execute("""
            INSERT INTO "artist" ("artist_id", "artist_name", "artist_genre")
            SELECT
                nextval('artist_id_seq'), 
                -- Combine two random words for artist_name
                (array['Hellfire', 'Cursed', 'My dear', 'Black'])[floor(random() * 4) + 1] || ' ' || 
                (array['Death', 'Angel', 'String', 'Coffin'])[floor(random() * 4) + 1],
                (array['rock', 'heavy metal', 'industrial metal', 'alternative rock'])[floor(random() * 4) + 1]
            FROM generate_series(1, %s);
            """, (number_of_operations,))
            self.conn.commit()
            return True  # Returns True if the insertion was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With An Artist Adding: {str(e)}")
            return False  # Returns False if insertion fails

    def truncate_artist_table(self):
        c = self.conn.cursor()
        try:
            # Insert data
            c.execute("""DELETE FROM "artist" """)
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With An Artist`s Data Deleting: {str(e)}")
            return False   # Returns False if insertion fails