class ModelPerformance:
    def __init__(self, db_model):
        self.conn = db_model.conn

    def add_performance(self, performance_id, festival_id, artist_id, start_time, finish_time):
        c = self.conn.cursor()
        try:
            # Check if client_id and room_number match parent tables
            c.execute('SELECT 1 FROM "festival" WHERE "festival_id" = %s', (festival_id,))
            festival_exists = c.fetchone()

            c.execute('SELECT 1 FROM "artist" WHERE "artist_id" = %s', (artist_id,))
            artist_exists = c.fetchone()

            if not festival_exists or not artist_exists:
                # Return an exception notification and throw an error
                return False  # Or throw an exception to process it further
            else:
                # All checks have passed, insert into booking_ticket
                c.execute(
                    'INSERT INTO "performance" ("performance_id", '
                    '"start_time", "finish_time", "festival_id", "artist_id") VALUES (%s, %s, %s, %s, %s)',
                    (performance_id, start_time, finish_time, festival_id, artist_id,))
                self.conn.commit()
                return True
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Adding A Performance: {str(e)}")
            return False

    def get_all_performance(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "performance"')
        return c.fetchall()

    def update_performance(self, performance_id, festival_id, artist_id, start_time, finish_time):
        c = self.conn.cursor()
        try:
            # Attempting to update a record
            c.execute('UPDATE "performance" SET "start_time" = %s, '
                      '"finish_time" = %s, "festival_id" = %s, "artist_id" = %s  WHERE  "performance_id" = %s',
                      (festival_id, artist_id, start_time, finish_time, performance_id))
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            # Handling an error if the update failed
            self.conn.rollback()
            print(f"Error With Updating A Performance: {str(e)}")
            return False   # Returns False if insertion fails

    def delete_performance(self, performance_id):
        c = self.conn.cursor()
        try:
            # Attempting to update a record
            c.execute('DELETE FROM "performance" WHERE "performance_id" = %s', (performance_id,))
            self.conn.commit()
            return True  # Returns True if the update was successful
        except Exception as e:
            # Handling an error in case the deletion failed
            self.conn.rollback()
            print(f"Error With Deleting A Performance: {str(e)}")
            return False   # Returns False if insertion fails

    def check_performance_existence(self, performance_id):
        c = self.conn.cursor()
        c.execute('SELECT 1 FROM "performance" WHERE "performance_id" = %s', (performance_id,))
        return bool(c.fetchone())

    def create_performance_sequence(self):
        c = self.conn.cursor()
        c.execute("""
            DO $$
            DECLARE
                max_id INT;
            BEGIN
                -- Find the maximum existing performance_id
                SELECT COALESCE(MAX(performance_id), 0) INTO max_id FROM performance;

                -- Check if the sequence exists
                IF NOT EXISTS (
                    SELECT 1 
                    FROM pg_sequences 
                    WHERE schemaname = 'public' AND sequencename = 'performance_id_seq'
                ) THEN
                    -- Create a new sequence starting after the max_id
                    EXECUTE 'CREATE SEQUENCE performance_id_seq START WITH ' || (max_id + 1);
                ELSE
                    -- Reset the existing sequence to start after the max_id
                    EXECUTE 'ALTER SEQUENCE performance_id_seq RESTART WITH ' || (max_id + 1);
                END IF;
            END $$;
        """)
        self.conn.commit()

    def generate_rand_performance_data(self, number_of_operations):
        c = self.conn.cursor()
        try:
            c.execute("""
                INSERT INTO "performance" ("performance_id", "festival_id", "artist_id", "start_time", "finish_time")
                SELECT 
                    nextval('performance_id_seq'), 
                    -- Random festival_id
                    floor(random() * (SELECT max("festival_id") FROM "festival") + 1),
                    --  Random artist_id
                    floor(random() * (SELECT max("artist_id") FROM "artist") + 1),
                    TO_CHAR('00:00:00'::time + (random() * interval '23 hours'), 'HH24:MI:SS')::time as start_time,
                    TO_CHAR('00:00:00'::time + (random() * interval '23 hours') + interval '2 hours', 'HH24:MI:SS')::time as finish_time
                FROM generate_series(1, %s);
            """, (number_of_operations,))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Performance Adding: {str(e)}")
            return False

    def truncate_performance_table(self):
        c = self.conn.cursor()
        try:
            # Insert data
            c.execute("""DELETE FROM "performance" """)
            self.conn.commit()
            return True  # Returns True if the insertion was successful
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Deleting A Performance Data: {str(e)}")
            return False  # Returns False if insertion fails