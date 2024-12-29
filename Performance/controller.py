class ControllerPerformance:
    def __init__(self, model_Performance, view_Performance):
        self.model_Performance = model_Performance
        self.view_Performance = view_Performance

    def add_Performance(self):
        # Request the ID of the reservation to be updated
        Performance_ID = self.view_Performance.get_Performance_id()

        Festival_ID, Artist_ID, Start_time, Finish_time = (
            self.view_Performance.get_Performance_input())
        # Call a method from the Model class to add a Performance
        success = (self.model_Performance.add_Performance
                   (Performance_ID, Festival_ID, Artist_ID, Start_time, Finish_time))

        # Display a message about the result of the operation
        if success:
            self.view_Performance.show_Performance_message("Successfully Add New Performance")
        else:
            self.view_Performance.show_Performance_message("Performance Don`t Deleted")

    def view_Performances(self):
        # Call a method from the Model class to retrieve all reservations
        performance = self.model_Performance.get_all_Performance()

        # Display reservations via a method from the View class
        self.view_Performance.show_Performance(performance)

    def update_Performance(self):
        # Request the ID of the Performance to be updated
        Performance_ID = self.view_Performance.get_Performance_id()

        # Check if there is a reservation with the specified ID
        Performance_exists = self.model_Performance.check_Performance_existence(Performance_ID)

        if Performance_exists:
            # Request updated Performance details from the user
            Festival_ID, Artist_ID, Start_time, Finish_time = (
                self.view_Performance.get_Performance_input())
            # Call a method from the Model class to update the reservation
            success = (self.model_Performance.update_Performance
                       (Performance_ID, Festival_ID, Artist_ID, Start_time, Finish_time))

            # Display a message about the result of the operation
            if success:
                self.view_Performance.show_Performance_message("Successfully Updated a Performance")
            else:
                self.view_Performance.show_Performance_message("Performance Don`t Updated")
        else:
            self.view_Performance.show_Performance_message("It does`nt Exist A Performance With This ID")

    def delete_Performance(self):
        # Request the ID of the Performance to be deleted
        Performance_id = self.view_Performance.get_Performance_id()

        # Check if there is a reservation with the specified ID
        Performance_exists = self.model_Performance.check_Performance_existence(Performance_id)

        if Performance_exists:
            # Call a method from the Model class to delete a Performance
            success = self.model_Performance.delete_Performance(Performance_id)

            # Display a message about the result of the operation
            if success:
                self.view_Performance.show_Performance_message("Successfully Delete A Performance")
            else:
                self.view_Performance.show_Performance_message("A Performance Don`t deleted")
        else:
            self.view_Performance.show_Performance_message("Performance with the specified ID does not exist.")

    def create_Performance_sequence(self):
        # Call method create_Performance_sequence from class ModelPerformance
        self.model_Performance.create_Performance_sequence()
        self.view_Performance.show_Performance_message("Successfully Created A Performance Sequence")

    def generate_rand_Performance_data(self, number_of_operations):
        # Call method generate_rand_Performance_data from class ModelPerformance
        success = self.model_Performance.generate_rand_Performance_data(number_of_operations)

        if success:
            self.view_Performance.show_Performance_message(
                f"{number_of_operations} Successfully Created Performances")
        else:
            self.view_Performance.show_Performance_message("Performance Does`nt Created")

    def truncate_Performance_table(self):
        # Call the method of the corresponding model
        success = self.model_Performance.truncate_Performance_table()

        if success:
            self.view_Performance.show_Performance_message("All Performances Data Successfully Deleted")
        else:
            self.view_Performance.show_Performance_message("All Performances Data Does`nt Deleted")