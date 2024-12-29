class ModelAnalytics:
    def __init__(self, db_model):
        self.conn = db_model.conn

    def popular_artist(self):
        c = self.conn.cursor()
        try:
            c.execute("""
                    SELECT "artist_id", "artist_name", "num_performances"
                    FROM (
                        SELECT pr."artist_id", pr."artist_name", 
                        COUNT(*) AS num_performances,
                        DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
                        FROM "performance" p
                        JOIN "artist" pr ON p."artist_id" = pr."artist_id"
                        GROUP BY pr."artist_id", pr."artist_name"
                    ) ranked
                    WHERE rnk = 1;
            """)

            popular_artist_data = c.fetchall() # Fetch the data from the query

            self.conn.commit()
            return popular_artist_data
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Analytics Of Popular Artist: {str(e)}")
            return None

    def number_of_performance(self):
        c = self.conn.cursor()
        try:
            c.execute("""
                        SELECT 
                            p."performance_id",
                            p."festival_id",
                            p."artist_id",
                            pr."artist_name",
                            pr."artist_genre",
                            p."start_time",
                            p."finish_time"
                        FROM 
                            "performance" p
                        JOIN 
                            "artist" pr ON p."artist_id" = pr."artist_id"
                        ORDER BY 
                            p."performance_id" DESC -- Sort by the most recently added
                        LIMIT 10;  -- Return only the 10 most recent performances
            """)

            number_of_performance_data = c.fetchall()  # Отримати дані з запиту

            self.conn.commit()
            return number_of_performance_data
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Analytics Of Number Of Performance: {str(e)}")
            return None

    def genre_analytics(self):
        c = self.conn.cursor()
        try:
            c.execute("""
                    WITH GenreRank AS (
                       SELECT
                           pr."artist_genre" AS popular_genre,
                           COUNT(*) AS num_performances,
                           DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
                       FROM
                           "performance" p
                       JOIN
                           "artist" pr ON p."artist_id" = pr."artist_id"
                       GROUP BY
                           pr."artist_genre"
                   )
                   SELECT
                       popular_genre,
                       num_performances
                   FROM
                       GenreRank
                   WHERE
                       rnk = 1;
            """)

            genre_data = c.fetchall()  # Отримати дані з запиту

            self.conn.commit()
            return genre_data
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Analytics Of Genre: {str(e)}")
            return None
