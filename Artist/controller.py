class ControllerArtist:
    def __init__(self, model_artist, view_artist):
        self.model_artist = model_artist
        self.view_artist = view_artist

    def add_artist(self):
        # Requesting Artist data from the user

        artist_id = self.view_artist.get_artist_id()
        artist_name = self.view_artist.get_artist_name()
        artist_genre = self.view_artist.get_artist_genre()

        if self.model_artist.add_artist(artist_id, artist_name, artist_genre):
            self.view_artist.show_artist_message("Successfully Add An Artist.")
        else:
            self.view_artist.show_artist_message("Artist Not Added.")

    def view_artists(self):
        # Call a method from the Model class to get all the Artist
        artists = self.model_artist.get_all_artists()

        # Display Artists via a method from the ViewArtist class (assuming you have such a class)
        self.view_artist.show_artists(artists)

    def update_artist(self):
        # Request the ID of the artist to be updated
        artist_id = self.view_artist.get_artist_id()

        # Check if there is an artist with the specified number
        artist_exists = self.model_artist.check_artist_existence(artist_id)

        if artist_exists:
            # Request updated Artist data from the user
            artist_name = self.view_artist.get_artist_name()
            artist_genre = self.view_artist.get_artist_genre()

            # Call a method from the Model class to update the Artist info
            success = self.model_artist.update_artist(artist_id, artist_name, artist_genre)

            # Display a message about the result of the operation
            if success:
                self.view_artist.show_artist_message("Successfully Update An Artist")
            else:
                self.view_artist.show_artist_message("Artist Not Updated.")
        else:
            self.view_artist.show_artist_message("It Does Not Exist An Artist With This ID")

    def delete_artist(self):
        # Request the ID of the artist to be deleted
        artist_id = self.view_artist.get_artist_id()

        # Check if there is an artist with the specified ID
        artist_exists = self.model_artist.check_artist_existence(artist_id)

        if artist_exists:
            # Call a method from the Model class to delete an artist
            success = self.model_artist.delete_artist(artist_id)

            # Display a message about the result of the operation
            if success:
                self.view_artist.show_artist_message("successfully Deleted An Artist")
            else:
                self.view_artist.show_artist_message("Artist Don`t Deleted")
        else:
            self.view_artist.show_artist_message("It Does Not Exist An Artist With This ID")

    def create_artist_sequence(self):
        # Call method create_artist_sequence from class ModelArtist
        self.model_artist.create_artist_sequence()
        self.view_artist.show_artist_message("Successfully Created Artist Sequence")

    def generate_rand_artist_data(self, number_of_operations):
        # Call the generate_rand_artist_data method from the ModelArtist class
        success = self.model_artist.generate_rand_artist_data(number_of_operations)

        if success:
            self.view_artist.show_artist_message(f"{number_of_operations} Artists Created successfully!")
        else:
            self.view_artist.show_artist_message("Failed To Create Artists.")

    def truncate_artist_table(self):
        # Call the method of the corresponding model
        success = self.model_artist.truncate_artist_table()

        if success:
            self.view_artist.show_artist_message("All Artists Data Deleted")
        else:
            self.view_artist.show_artist_message("Artist Data Not Deleted")