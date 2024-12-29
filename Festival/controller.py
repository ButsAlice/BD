
class ControllerFestival:
    def __init__(self, model_Festival, view_Festival):
        self.model_Festival = model_Festival
        self.view_Festival = view_Festival

    def add_Festival(self):
        Festival_id = self.view_Festival.get_Festival_id()
        name, price, city = self.view_Festival.get_Festival_input()
        if self.model_Festival.add_Festival(Festival_id, name, price, city):
            self.view_Festival.show_Festival_message("Successfully Added A Festival")
        else:
            self.view_Festival.show_Festival_message("Festival Don`t Added")

    def view_Festivals(self):
        Festivals = self.model_Festival.get_all_Festivals()
        self.view_Festival.show_Festivals(Festivals)

    def update_Festival(self):
        # Request the ID of the Festival to be updated
        Festival_id = self.view_Festival.get_Festival_id()

        # Check if there is a Festival with the specified ID
        Festival_exists = self.model_Festival.check_Festival_existence(Festival_id)

        if Festival_exists:
            # Request updated Festival data from the user
            name, price, city = self.view_Festival.get_Festival_input()
            # Call a method from the Model class to update the Festival
            success = (self.model_Festival.update_Festival(Festival_id, name, price, city))

            # Display a message about the result of the operation
            if success:
                self.view_Festival.show_Festival_message("Successfully Updated A Festival")
            else:
                self.view_Festival.show_Festival_message("Festival Don`t Updated")
        else:
            self.view_Festival.show_Festival_message("It Does`nt Exist A Festival With This ID")

    def delete_Festival(self):
        Festival_id = self.view_Festival.get_Festival_id()

        # Check if there is a reservation with the specified ID
        Festival_exists = self.model_Festival.check_Festival_existence(Festival_id)

        if Festival_exists:
            if self.model_Festival.delete_Festival(Festival_id):
                self.view_Festival.show_Festival_message("Successfully Deleted A Festival")
            else:
                self.view_Festival.show_Festival_message("Festival Don`t Deleted")
        else:
            self.view_Festival.show_Festival_message("It Does`nt Exist A Festival With This ID")

    def create_Festival_sequence(self):
        # Call the create_client_sequence method from the ModelFestival class
        self.model_Festival.create_Festival_sequence()
        self.view_Festival.show_Festival_message("Successfully Generates Festival`s Sequence")

    def generate_rand_Festival_data(self, number_of_operations):
        # Call the generate_rand_Festival_data method from the ModelFestival class
        success = self.model_Festival.generate_rand_Festival_data(number_of_operations)

        if success:
            self.view_Festival.show_Festival_message(f"{number_of_operations} Successfully Generates Festival")
        else:
            self.view_Festival.show_Festival_message("Festival Don`t Created")

    def truncate_Festival_table(self):
        # Call the method of the corresponding model
        success = self.model_Festival.truncate_Festival_table()

        if success:
            self.view_Festival.show_Festival_message("Successfully Deleted All Festival`s Data")
        else:
            self.view_Festival.show_Festival_message("Festival All Data Don`t delete`t")