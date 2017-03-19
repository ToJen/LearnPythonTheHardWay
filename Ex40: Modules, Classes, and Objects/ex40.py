class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "You live in a zoo"])

happy_farell = Song(["Clap your hands if you feel like that's what you wanna do",
                     "Clap your hands if you know that happiness is the truth"])

happy_bday.sing_me_a_song()
happy_farell.sing_me_a_song()