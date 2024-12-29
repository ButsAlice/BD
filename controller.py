from model import Model

from Performance.view import ViewPerformance
from Performance.model import ModelPerformance
from Performance.controller import ControllerPerformance

from Festival.view import ViewFestival
from Festival.model import ModelFestival
from Festival.controller import ControllerFestival

from Performer.view import ViewPerformer
from Performer.model import ModelPerformer
from Performer.controller import ControllerPerformer

from Analytics.view import ViewAnalytics
from Analytics.model import ModelAnalytics
from Analytics.controller import ControllerAnalytics


class Controller:
    def __init__(self):
        self.model = Model()
        self.view_Performance = ViewPerformance()
        self.view_Festival = ViewFestival()
        self.view_Performer = ViewPerformer()
        self.view_analytics = ViewAnalytics()

        self.model_Performance = ModelPerformance(self.model)
        self.model_Festival = ModelFestival(self.model)
        self.model_Performer = ModelPerformer(self.model)
        self.model_analytics = ModelAnalytics(self.model)

        self.controller_Performance = ControllerPerformance(self.model_Performance, self.view_Performance)
        self.controller_Festival = ControllerFestival(self.model_Festival, self.view_Festival)
        self.controller_Performer = ControllerPerformer(self.model_Performer, self.view_Performer)
        self.controller_analytics = ControllerAnalytics(self.model_analytics, self.view_analytics)

    def run(self):
        methods = {
            '1': self.controller_Performance.add_Performance,
            '2': self.controller_Performance.view_Performances,
            '3': self.controller_Performance.update_Performance,
            '4': self.controller_Performance.delete_Performance,
            '5': self.controller_Festival.add_Festival,
            '6': self.controller_Festival.view_Festivals,
            '7': self.controller_Festival.update_Festival,
            '8': self.controller_Festival.delete_Festival,
            '9': self.controller_Performer.add_Performer,
            '10': self.controller_Performer.view_Performers,
            '11': self.controller_Performer.update_Performer,
            '12': self.controller_Performer.delete_Performer,
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
        "Add New Performance",
        "Show Performances",
        "Renewal Performance",
        "Remove Performance",
        "Add New Festival",
        "Show Festivals",
        "Renewal Festival",
        "Remove Festival",
        "Add New Performer",
        "Show Performers",
        "Renewal Performer",
        "Remove Performer",
        "Create Data By Random",
        "Delete All Data",
        "View Analytics",
        "Exit"
    ]

    def show_menu(self):
        self.view_Performance.show_Performance_message("\nMain Menu:")
        for idx, option in enumerate(self.MENU_OPTIONS, start=1):
            self.view_Performance.show_Performance_message(f"{idx}. {option}")
        return input("Choose an action : ")

    def create_performer_sequence(self):
        self.controller_Performer.create_Performer_sequence()

    def generate_rand_performer_data(self, number_of_operations):
        self.controller_Performer.generate_rand_Performer_data(number_of_operations)

    def create_festival_sequence(self):
        self.controller_Festival.create_Festival_sequence()

    def generate_rand_festival_data(self, number_of_operations):
        self.controller_Festival.generate_rand_Festival_data(number_of_operations)

    def create_performance_sequence(self):
        self.controller_Performance.create_Performance_sequence()

    def generate_rand_performance_data(self, number_of_operations):
        self.controller_Performance.generate_rand_Performance_data(number_of_operations)

    def generate_rand_data(self):
        number_of_operations = int(input("Input Number Of Generations: "))
        self.create_performer_sequence()
        self.generate_rand_performer_data(number_of_operations)
        self.create_festival_sequence()
        self.generate_rand_festival_data(number_of_operations)
        self.create_performance_sequence()
        self.generate_rand_performance_data(number_of_operations)

    def truncate_all_tables(self):
        if input("Confirm The Action. Type Yes or No: ") == "Yes":
            self.controller_Performance.truncate_Performance_table()
            self.controller_Festival.truncate_Festival_table()
            self.controller_Performer.truncate_Performer_table()
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
