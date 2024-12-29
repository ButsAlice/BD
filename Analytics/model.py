class ModelAnalytics:
    def __init__(self, db_model):
        self.conn = db_model.conn

    def popular_artist(self):
        c = self.conn.cursor()
        try:
            c.execute("""
                    SELECT "Artist_ID", "name", "surname", "num_performances"
                    FROM (
                        SELECT pr."Artist_ID", pr."name", pr."surname", 
                        COUNT(*) AS num_performances,
                    DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
                    FROM "Perfomance" p
                    JOIN "Performer" pr ON p."Artist_ID" = pr."Artist_ID"
                    GROUP BY pr."Artist_ID", pr."name", pr."surname"
                    ) ranked
                    WHERE rnk = 1;

                    """)

            popular_artist_data = c.fetchall()  # Get data from the query

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
                            p."Preformance_ID",
                            p."Festival_ID",
                            p."Artist_ID",
                            pr."name" AS artist_name,
                            pr."surname" AS artist_surname,
                            p."Start_time",
                            p."Finish_time"
                        FROM 
                            "Perfomance" p
                        JOIN 
                            "Performer" pr ON p."Artist_ID" = pr."Artist_ID"
                        WHERE 
                            p."Start_time" >= CURRENT_DATE - INTERVAL '1 month';

                        """)

            number_of_performance_data = c.fetchall()  # Get data from the query

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
                           pr."genre" AS popular_genre,
                           COUNT(*) AS num_performances,
                           DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
                       FROM
                           "Perfomance" p
                       JOIN
                           "Performer" pr ON p."Artist_ID" = pr."Artist_ID"
                       GROUP BY
                           pr."genre"
                   )
                   SELECT
                       popular_genre,
                       num_performances
                   FROM
                       GenreRank
                   WHERE
                       rnk = 1;
                        """)

            genre_data = c.fetchall()  # Get data from the query

            self.conn.commit()
            return genre_data
        except Exception as e:
            self.conn.rollback()
            print(f"Error With Analytics Of Genre: {str(e)}")
            return None
