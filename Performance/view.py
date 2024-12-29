class ViewPerformance:

    def show_Performance(self, Performances):
        print("Performance:")
        for Performance in Performances:
            print(
                f"Performance ID: {Performance[0]}, Festival ID: {Performance[1]}, Artis ID: {Performance[2]}, "
                f"Start time: {Performance[3]}, Finish time: {Performance[4]}")

    def get_Performance_input(self):
        Festival_ID = int(input("Input Festival ID: "))
        Artist_ID = int(input("Input Artist ID: "))
        Start_time = input("Input start date (YYYY-MM-DD): ")
        Finish_time = input("Input finish date (YYYY-MM-DD): ")
        return Festival_ID, Artist_ID, Start_time, Finish_time

    def get_Performance_id(self):
        return int(input("Input Performance ID: "))

    def show_Performance_message(self, message):
        print(message)