class ViewArtist:
    def show_artists(self,artists):
        print("Artists:")
        for artist in artists:
            print(f"artist_id: {artist[0]}, artist_name: {artist[1]},  artist_genre: {artist[2]}")

    def get_artist_name(self):
        artist_name = input("Input name: ")
        return artist_name

    def get_artist_genre(self):
        artist_genre = input("Input genre: ")
        return artist_genre

    def get_artist_id(self):
        return int(input("Input artist_id: "))

    def show_artist_message(self, message):
        print(message)