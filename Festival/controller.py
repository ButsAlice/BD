class ControllerFestival:
    def __init__(self, model_festival, view_festival):
        self.model_festival = model_festival
        self.view_festival = view_festival

    def add_festival(self):
        festival_id = self.view_festival.get_festival_id()
        fest_name, fest_date, fest_place = self.view_festival.get_festival_input()
        if self.model_festival.add_festival(festival_id, fest_name, fest_date, fest_place):
            self.view_festival.show_festival_message("Successfully Added A Festival")
        else:
            self.view_festival.show_festival_message("Festival Not Added")

    def view_festivals(self):
        festivals = self.model_festival.get_all_festivals()
        self.view_festival.show_festivals(festivals)

    def update_festival(self):
        festival_id = self.view_festival.get_festival_id()

        # Check if the festival exists
        festival_exists = self.model_festival.check_festival_existence(festival_id)

        if festival_exists:
            # Get updated festival data
            fest_name, fest_date, fest_place = self.view_festival.get_festival_input()
            # Update festival
            success = self.model_festival.update_festival(festival_id, fest_name, fest_date, fest_place)

            if success:
                self.view_festival.show_festival_message("Successfully Updated A Festival")
            else:
                self.view_festival.show_festival_message("Festival Not Updated")
        else:
            self.view_festival.show_festival_message("Festival Does Not Exist With This ID")

    def delete_festival(self):
        festival_id = self.view_festival.get_festival_id()

        # Check if the festival exists
        festival_exists = self.model_festival.check_festival_existence(festival_id)

        if festival_exists:
            if self.model_festival.delete_festival(festival_id):
                self.view_festival.show_festival_message("Successfully Deleted A Festival")
            else:
                self.view_festival.show_festival_message("Festival Not Deleted")
        else:
            self.view_festival.show_festival_message("Festival Does Not Exist With This ID")

    def create_festival_sequence(self):
        self.model_festival.create_festival_sequence()
        self.view_festival.show_festival_message("Successfully Generated Festival Sequence")

    def generate_rand_festival_data(self, number_of_operations):
        success = self.model_festival.generate_rand_festival_data(number_of_operations)

        if success:
            self.view_festival.show_festival_message(f"{number_of_operations} Festivals Successfully Generated")
        else:
            self.view_festival.show_festival_message("Festival Not Created")

    def truncate_festival_table(self):
        success = self.model_festival.truncate_festival_table()

        if success:
            self.view_festival.show_festival_message("Successfully Deleted All Festival Data")
        else:
            self.view_festival.show_festival_message("Festival Data Not Deleted")
