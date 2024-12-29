class ViewPerformer:
    def show_Performers(self, Performers):
        print("Artists:")
        for Performer in Performers:
            print(f"Artist_ID: {Performer[0]}, Artist name: {Performer[1]}, Artist surname: {Performer[2]}, genre: {Performer[3]}")

    def get_Artist_name(self):
        name = input("Input name: ")
        return name

    def get_Artist_surname(self):
        surname = input("Input surname: ")
        return surname

    def get_genre(self):
        genre = input("Input genre: ")
        return genre

    def get_Artist_ID(self):
        return int(input("Input Artist_ID: "))

    def show_Performer_message(self, message):
        print(message)