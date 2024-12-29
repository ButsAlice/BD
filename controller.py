from model import Model

from Performance.view import ViewPerformance
from Performance.model import ModelPerformance
from Performance.controller import ControllerPerformance

from Festival.view import ViewFestival
from Festival.model import ModelFestival
from Festival.controller import ControllerFestival

from Artist.view import ViewArtist
from Artist.model import ModelArtist
from Artist.controller import ControllerArtist

from Analytics.view import ViewAnalytics
from Analytics.model import ModelAnalytics
from Analytics.controller import ControllerAnalytics


class Controller:
    def __init__(self):
        self.model = Model()
        self.view_performance = ViewPerformance()
        self.view_festival = ViewFestival()
        self.view_artist = ViewArtist()
        self.view_analytics = ViewAnalytics()

        self.model_performance = ModelPerformance(self.model)
        self.model_festival = ModelFestival(self.model)
        self.model_artist = ModelArtist(self.model)
        self.model_analytics = ModelAnalytics(self.model)

        self.controller_performance = ControllerPerformance(self.model_performance, self.view_performance)
        self.controller_festival = ControllerFestival(self.model_festival, self.view_festival)
        self.controller_artist = ControllerArtist(self.model_artist, self.view_artist)
        self.controller_analytics = ControllerAnalytics(self.model_analytics, self.view_analytics)

    def run(self):
        methods = {
            '1': self.controller_artist.add_artist,
            '2': self.controller_performance.add_performance,
            '3': self.controller_festival.add_festival,
            '4': self.controller_artist.view_artists,
            '5': self.controller_performance.view_performances,
            '6': self.controller_festival.view_festivals,
            '7': self.controller_artist.update_artist,
            '8': self.controller_performance.update_performance,
            '9': self.controller_festival.update_festival,
            '10': self.controller_artist.delete_artist,
            '11': self.controller_performance.delete_performance,
            '12': self.controller_festival.delete_festival,
            '13': self.generate_rand_data,
            '14': self.truncate_all_tables,
            '15': self.display_analytics
        }

        while True:
            choice = self.show_menu()

            if choice in methods:
                methods[choice]()
            elif choice == '16':
                break

    MENU_OPTIONS = [
        "Add New Artist",
        "Add New Performance",
        "Add New Festival",
        "Show Artists",
        "Show Performances",
        "Show Festivals",
        "Update Artist",
        "Update Performance",
        "Update Festival",
        "Remove Artist",
        "Remove Performance",
        "Remove Festival",
        "Create Data By Random",
        "Delete All Data",
        "View Analytics",
        "Exit"
    ]

    def show_menu(self):
        self.view_performance.show_performance_message("\nMain Menu:")
        for idx, option in enumerate(self.MENU_OPTIONS, start=1):
            self.view_performance.show_performance_message(f"{idx}. {option}")
        return input("Choose an action : ")

    def create_artist_sequence(self):
        self.controller_artist.create_artist_sequence()

    def generate_rand_artist_data(self, number_of_operations):
        self.controller_artist.generate_rand_artist_data(number_of_operations)

    def create_festival_sequence(self):
        self.controller_festival.create_festival_sequence()

    def generate_rand_festival_data(self, number_of_operations):
        self.controller_festival.generate_rand_festival_data(number_of_operations)

    def create_performance_sequence(self):
        self.controller_performance.create_performance_sequence()

    def generate_rand_performance_data(self, number_of_operations):
        self.controller_performance.generate_rand_performance_data(number_of_operations)

    def generate_rand_data(self):
        number_of_operations = int(input("Input Number Of Generations: "))
        self.create_artist_sequence()
        self.generate_rand_artist_data(number_of_operations)
        self.create_festival_sequence()
        self.generate_rand_festival_data(number_of_operations)
        self.create_performance_sequence()
        self.generate_rand_performance_data(number_of_operations)

    def truncate_all_tables(self):
        if input("Confirm The Action. Type Yes or No: ") == "Yes":
            self.controller_performance.truncate_performance_table()
            self.controller_festival.truncate_festival_table()
            self.controller_artist.truncate_artist_table()
        else:
            print("Ok")

    def display_analytics(self):
        print("-------------------------------------------------------------------------------")
        self.controller_analytics.popular_artist()
        print("-------------------------------------------------------------------------------")
        self.controller_analytics.number_of_performance()
        print("-------------------------------------------------------------------------------")
        self.controller_analytics.genre_analytics()
        print("-------------------------------------------------------------------------------")