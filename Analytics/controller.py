class ControllerAnalytics:
    def __init__(self, model_analytics, view_analytics):
        self.model_analytics = model_analytics
        self.view_analytics = view_analytics

    def popular_artist(self):
        # Get analytical data
        popular_artist_data = self.model_analytics.popular_artist()

        # Show results
        if popular_artist_data:
            self.view_analytics.display_popular_artist(popular_artist_data)
        else:
            print("Error With Analytics Implemetation")

    def number_of_performance(self):
        # Do analytics
        number_of_performance_data = self.model_analytics.number_of_performance()

        # Show results
        if number_of_performance_data:
            self.view_analytics.display_number_of_performance(number_of_performance_data)
        else:
            print("Error With Analytics Implemetation")

    def genre_analytics(self):
        # Do analytics
        genre_analytics_data = self.model_analytics.genre_analytics()

        # Show results
        if genre_analytics_data is not None:
            self.view_analytics.display_genre_analytics(genre_analytics_data)
        else:
            print("Error With Analytics Implemetation")
