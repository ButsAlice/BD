class ControllerPerformer:
    def __init__(self, model_Performer, view_Performer):
        self.model_Performer = model_Performer
        self.view_Performer = view_Performer

    def add_Performer(self):
        # Requesting Performer data from the user

        Artist_ID = self.view_Performer.get_Artist_ID()
        name = self.view_Performer.get_Artist_name()
        surname= self.view_Performer.get_Artist_surname()
        genre = self.view_Performer.get_genre()

        if self.model_Performer.add_Performer(Artist_ID, name, surname, genre):
            self.view_Performer.show_Performer_message("Successfully Add An Artist.")
        else:
            self.view_Performer.show_Performer_message("Artist Not Added.")

    def view_Performers(self):
        # Call a method from the Model class to get all the Performer
        Performers = self.model_Performer.get_all_Performers()

        # Display Performers via a method from the ViewPerformer class (assuming you have such a class)
        self.view_Performer.show_Performers(Performers)

    def update_Performer(self):
        # Request the ID of the artist to be updated
        Artist_ID = self.view_Performer.get_Artist_ID()

        # Check if there is a Performer with the specified number
        Performer_exists = self.model_Performer.check_Performer_existence(Artist_ID)

        if Performer_exists:
            # Request updated Artist data from the user
            name = self.view_Performer.get_Artist_name()
            surname = self.view_Performer.get_Artist_surname()
            genre = self.view_Performer.get_genre()

            # Call a method from the Model class to update the Artist info
            success = self.model_Performer.update_Performer(Artist_ID, name, surname, genre)

            # Display a message about the result of the operation
            if success:
                self.view_Performer.show_Performer_message("Successfully Update An Artist")
            else:
                self.view_Performer.show_Performer_message("Artist Not Updated.")
        else:
            self.view_Performer.show_Performer_message("It Does Not Exist An Artist With This ID")

    def delete_Performer(self):
        # Request the ID of the Performer to be deleted
        Artist_ID = self.view_Performer.get_Artist_ID()

        # Check if there is a Performer with the specified ID
        Performer_exists = self.model_Performer.check_Performer_existence(Artist_ID)

        if Performer_exists:
            # Call a method from the Model class to delete a Performer
            success = self.model_Performer.delete_Performer(Artist_ID)

            # Display a message about the result of the operation
            if success:
                self.view_Performer.show_Performer_message("successfully Deleted A Performer")
            else:
                self.view_Performer.show_Performer_message("Performer Don`t Deleted")
        else:
            self.view_Performer.show_Performer_message("It Does Not Exist A Performer With This ID")

    def create_Performer_sequence(self):
        # Call method create_Performer_sequence from class ModelPerformer
        self.model_Performer.create_Performer_sequence()
        self.view_Performer.show_Performer_message("Successfully Created Performer Sequence")

    def generate_rand_Performer_data(self, number_of_operations):
        # Call the generate_rand_Performer_data method from the ModelPerformer class
        success = self.model_Performer.generate_rand_Performer_data(number_of_operations)

        if success:
            self.view_Performer.show_Performer_message(f"{number_of_operations} Performers Created successfully!")
        else:
            self.view_Performer.show_Performer_message("Failed To Create Performers.")

    def truncate_Performer_table(self):
        # Call the method of the corresponding model
        success = self.model_Performer.truncate_Performer_table()

        if success:
            self.view_Performer.show_Performer_message("All Performers Data Deleted")
        else:
            self.view_Performer.show_Performer_message("Performer Data Not Deleted")