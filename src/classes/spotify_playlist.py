from spotify_track import SpotifyTrack

class SpotifyPlaylist:

    def __init__(self):
        self.playlist_id = None
        self.name = None
        self.tracks = set()
        self.total = len(self.tracks)

    def add_track(self, track):
        self.tracks.add(track)
        self.total = len(self.tracks)

    def remove_track(self, track):
        if track in self.tracks:
            self.tracks.remove(track)
            self.total = len(self.tracks)
        else:
            return "Track not found in playlist, unable to remove"