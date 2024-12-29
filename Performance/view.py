class ViewPerformance:

    def show_performance(self, performances):
        print("Performance:")
        for performance in performances:
            print(
                f"Performance ID: {performance[0]}, Start time: {performance[1]}, Finish time: {performance[2]}, "
                f"Festival ID: {performance[3]}, Artis ID: {performance[4]}")

    def get_performance_input(self):
        start_time = input("Input start time (HH:MM:SS): ")
        finish_time = input("Input finish time (HH:MM:SS): ")
        festival_id = int(input("Input Festival ID: "))
        artist_id = int(input("Input Artist ID: "))
        return start_time, finish_time, festival_id, artist_id

    def get_performance_id(self):
        return int(input("Input Performance ID: "))

    def show_performance_message(self, message):
        print(message)