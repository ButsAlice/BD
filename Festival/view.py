class ViewFestival:
    def show_festivals(self, festivals):
        print("Festivals:")
        for festival in festivals:
            print(f"ID: {festival[0]}, Name: {festival[1]}, Date: {festival[2]}, Place: {festival[3]}")

    def get_festival_input(self):
        fest_name = input("Input festival name: ")
        fest_date = input("Input festival date: ")
        fest_place = input("Input festival place: ")
        return  fest_name, fest_date, fest_place

    def get_festival_id(self):
        return int(input("Input festival id: "))

    def show_festival_message(self, message):
        print(message)
