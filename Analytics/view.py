class ViewAnalytics:
    def display_popular_artist(self, popular_artist_data):
        print("Найпопулярніші виконавці:")
        for row in popular_artist_data:
            Artist_ID, name, surname, num_performances = row
            print(f"ID: {Artist_ID}, ім'я та прізвище {name} {surname}, кількість виступів: {num_performances}")

    def display_number_of_performance(self, number_of_performance_data):
        print("Кількість виступів за останній місяць:")
        for row in number_of_performance_data:
            Preformace_ID, Festival_ID, Artist_ID, name, surname, Start_time, Finish_time  = row
            print(f"Виступ № {Preformace_ID}, № фестивалю: {Festival_ID}, артист:{name} {surname} ,початок та кінець: {Start_time} -> {Finish_time}")

    def display_genre_analytics(self, genre_analytics_data):
        print("Найчастіше використані жанри :")
        for row in genre_analytics_data:
            popular_genre, num_performances = row
            print( f"Жанр: {popular_genre}, Кількість: {num_performances} ")