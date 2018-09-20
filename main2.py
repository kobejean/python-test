class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        song = self
        playlist = [song]
        while isinstance(song.next, Song):
            print(song.name)
            if song.next in playlist:
                return True
            else:
                playlist.append(song.next)
                song = song.next

        return False

first = Song("Hello")
second = Song("Eye of the tiger")
second1 = Song("Eye of the tiger1")
second2 = Song("Eye of the tiger2")
second3 = Song("Eye of the tiger3")
second4 = Song("Eye of the tiger4")

first.next_song(second);
second.next_song(second1);
second1.next_song(second2);
second2.next_song(second3);
second3.next_song(second4);
second4.next_song(second3);


print(first.is_repeating_playlist())
