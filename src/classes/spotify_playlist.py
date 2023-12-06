from spotify_track import SpotifyTrack

class SpotifyPlaylist:

    def __init__(self, playlist_id, name):
        self.playlist_id = playlist_id
        self.name = name
        self.tracks = set()

    def add_track(self, track):
        self.tracks.add(track)

    def remove_track(self, track):
        if track in self.tracks:
            self.tracks.remove(track)
        else:
            return "Track not found in playlist, unable to remove"
