class ViewAnalytics:
    def display_popular_artist(self, popular_artist_data):
        print("Найпопулярніші виконавці:")
        for row in popular_artist_data:
            artist_id, artist_name, num_performances = row
            print(f"ID: {artist_id}, ім'я: {artist_name}, кількість виступів: {num_performances}")

    def display_number_of_performance(self, number_of_performance_data):
        print("Інформація про останні 10 доданих виступів")
        for row in number_of_performance_data:
            performance_id, festival_id, artist_id, artist_name, artist_genre, start_time, finish_time = row
            print(f"Виступ № {performance_id}, № фестивалю: {festival_id}, артист: {artist_name} ({artist_genre}), початок: {start_time}, кінець: {finish_time}")

    def display_genre_analytics(self, genre_analytics_data):
        print("Найчастіше використані жанри:")
        for row in genre_analytics_data:
            genre, num_performances = row
            print(f"Жанр: {genre}, Кількість виступів: {num_performances}")
