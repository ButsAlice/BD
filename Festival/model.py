class ModelFestival:
    def __init__(self, db_model):
        self.conn = db_model.conn

    def add_festival(self, festival_id, fest_name, fest_date, fest_place):
        c = self.conn.cursor()
        try:
            c.execute('INSERT INTO "festival" ("festival_id", "fest_name", "fest_date", "fest_place") VALUES (%s, %s, %s, %s)',
                      (festival_id, fest_name, fest_date, fest_place))
            self.conn.commit()
            return True  # Returns True if the operation is successful
        except Exception as e:
            self.conn.rollback()
            print(f"Помилка при додаванні фестивалю: {str(e)}")
            return False  # Returns False if the operation failed

    def get_all_festivals(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "festival"')
        return c.fetchall()

    def update_festival(self, festival_id, fest_name, fest_date, fest_place):
        c = self.conn.cursor()
        try:
            c.execute('UPDATE "festival" SET "fest_name" = %s, "fest_date" = %s, "fest_place" = %s WHERE "festival_id"=%s',
                      (fest_name, fest_date, fest_place, festival_id))
            self.conn.commit()
            return True   # Returns True if the operation is successful
        except Exception as e:
            self.conn.rollback()
            print(f"Помилка при оновленні фестивалю: {str(e)}")
            return False  # Returns False if the operation failed

    def delete_festival(self, festival_id):
        c = self.conn.cursor()
        try:
            c.execute("DELETE FROM festival WHERE festival_id = %s", (festival_id,))
            self.conn.commit()
            print(f"Festival {festival_id} successfully deleted.")
        except Exception as e:
            self.conn.rollback()
            if "violates foreign key constraint" in str(e):
                print(f"Festival {festival_id} cannot be deleted as it is associated with performances.")
            else:
                print(f"Error deleting festival: {str(e)}")

    def check_festival_existence(self, festival_id):
        c = self.conn.cursor()
        c.execute('SELECT 1 FROM "festival" WHERE "festival_id" = %s', (festival_id,))
        return bool(c.fetchone())

    def create_festival_sequence(self):
        # Creating or updating the sequence for festival_id
        c = self.conn.cursor()
        c.execute("""
               DO $$ 
               DECLARE 
                   max_id INT;
               BEGIN 
                   -- Знаходимо максимальний festival_id
                   SELECT COALESCE(MAX(festival_id), 0) INTO max_id FROM festival;

                   -- Перевіряємо чи існує послідовність
                   IF NOT EXISTS (
                       SELECT 1 FROM pg_sequences WHERE schemaname = 'public' AND sequencename = 'festival_festival_id_seq'
                   ) THEN
                       -- Створюємо нову послідовність для festival_id, починаючи з max_id + 1
                       EXECUTE 'CREATE SEQUENCE festival_festival_id_seq START WITH ' || (max_id + 1);
                   ELSE
                       -- Оновлюємо існуючу послідовність, щоб вона починалась з max_id + 1
                       EXECUTE 'ALTER SEQUENCE festival_festival_id_seq RESTART WITH ' || (max_id + 1);
                   END IF;
               END $$;
           """)
        self.conn.commit()

    def generate_rand_festival_data(self, number_of_operations):
        c = self.conn.cursor()
        try:
            # Inserting data into the festival table
            c.execute("""
               INSERT INTO "festival" ("festival_id", "fest_name", "fest_date", "fest_place")
               SELECT
                   nextval('festival_festival_id_seq'),  -- Використовуємо послідовність для генерації нового id
                   (array['Faint', 'Meteora', 'Bleach', 'Nevermind', 'Cherry Waves', 'Heart-Shaped Box'])[floor(random() * 6) + 1],
                   CURRENT_DATE + (floor(random() * 365) * interval '1 day'),
                   (array['London', 'Kyiv', 'Paris', 'Berlin', 'New York'])[floor(random() * 5) + 1]
               FROM generate_series(1, %s);
               """, (number_of_operations,))
            self.conn.commit()
            return True  # If insertion is successful
        except Exception as e:
            self.conn.rollback()
            print(f"Помилка при додаванні даних фестивалю: {str(e)}")
            return False  # If insertion failed

    def truncate_festival_table(self):
        c = self.conn.cursor()
        try:
            c.execute("DELETE FROM festival")   # Clear the festival table
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"Помилка при видаленні всіх даних фестивалю: {str(e)}")
            return False
