class ControllerPerformance:
    def __init__(self, model_performance, view_performance):
        self.model_performance = model_performance
        self.view_performance = view_performance

    def add_performance(self):
        # Request the ID of the performance to be updated
        performance_id = self.view_performance.get_performance_id()

        festival_id, artist_id, start_time, finish_time = (
            self.view_performance.get_performance_input())

        # Call a method from the Model class to add a performance
        success = (self.model_performance.add_performance
                   (performance_id, start_time, finish_time, festival_id, artist_id))

        # Display a message about the result of the operation
        if success:
            self.view_performance.show_performance_message("Successfully Added New Performance")
        else:
            self.view_performance.show_performance_message("Performance Not Added")

    def view_performances(self):
        # Call a method from the Model class to retrieve all performances
        performances = self.model_performance.get_all_performance()

        # Display performances via a method from the View class
        self.view_performance.show_performance(performances)

    def update_performance(self):
        # Request the ID of the performance to be updated
        performance_id = self.view_performance.get_performance_id()

        # Check if there is a performance with the specified ID
        performance_exists = self.model_performance.check_performance_existence(performance_id)

        if performance_exists:
            # Request updated performance details from the user
            festival_id, artist_id, start_time, finish_time = (
                self.view_performance.get_performance_input())
            # Call a method from the Model class to update the performance
            success = (self.model_performance.update_performance
                       (performance_id, festival_id, artist_id, start_time, finish_time))

            # Display a message about the result of the operation
            if success:
                self.view_performance.show_performance_message("Successfully Updated A Performance")
            else:
                self.view_performance.show_performance_message("Performance Not Updated")
        else:
            self.view_performance.show_performance_message("Performance With This ID Does Not Exist")

    def delete_performance(self):
        # Request the ID of the performance to be deleted
        performance_id = self.view_performance.get_performance_id()

        # Check if there is a performance with the specified ID
        performance_exists = self.model_performance.check_performance_existence(performance_id)

        if performance_exists:
            # Call a method from the Model class to delete a performance
            success = self.model_performance.delete_performance(performance_id)

            # Display a message about the result of the operation
            if success:
                self.view_performance.show_performance_message("Successfully Deleted A Performance")
            else:
                self.view_performance.show_performance_message("Performance Not Deleted")
        else:
            self.view_performance.show_performance_message("Performance With The Specified ID Does Not Exist")

    def create_performance_sequence(self):
        # Call method create_performance_sequence from class ModelPerformance
        self.model_performance.create_performance_sequence()
        self.view_performance.show_performance_message("Successfully Created Performance Sequence")

    def generate_rand_performance_data(self, number_of_operations):
        # Call method generate_rand_performance_data from class ModelPerformance
        success = self.model_performance.generate_rand_performance_data(number_of_operations)

        if success:
            self.view_performance.show_performance_message(
                f"{number_of_operations} Performances Successfully Created")
        else:
            self.view_performance.show_performance_message("Performance Not Created")

    def truncate_performance_table(self):
        # Call the method of the corresponding model
        success = self.model_performance.truncate_performance_table()

        if success:
            self.view_performance.show_performance_message("All Performances Data Successfully Deleted")
        else:
            self.view_performance.show_performance_message("All Performances Data Not Deleted")
