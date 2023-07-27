class Player:
    def __init__(self, name):
        self.name = name
        self.current_media = None
        self.volume = 50
        self.playing = False

    def play_media(self, media):
        self.current_media = media
        self.playing = True
        print(f"{self.name} is now playing {media}")

    def pause(self):
        if self.playing:
            self.playing = False
            print(f"{self.name} is paused")
        else:
            print(f"{self.name} is already paused")

    def stop(self):
        if self.playing:
            self.playing = False
            self.current_media = None
            print(f"{self.name} has stopped")
        else:
            print(f"{self.name} is already stopped")

    def change_volume(self, volume):
        if 0 <= volume <= 100:
            self.volume = volume
            print(f"{self.name} volume is now {volume}%")
        else:
            print("Volume should be between 0 and 100")

youtube = Player("YouTube")

youtube.play_media("Insidious")

youtube.change_volume(65)
