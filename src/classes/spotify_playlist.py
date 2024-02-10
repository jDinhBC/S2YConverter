from .spotify_track import SpotifyTrack

class SpotifyPlaylist:

    def __init__(self, playlist_id=None, name=None, tracks=None, total=None):
        self.playlist_id = playlist_id
        self.name = name
        self.tracks = tracks if tracks is not None else set()
        self.total = total if total is not None else len(self.tracks)

    def add_track(self, track):
        self.tracks.add(track)
        self.update_total()

    def remove_track(self, track):
        if track in self.tracks:
            self.tracks.remove(track)
            self.update_total()
        else:
            return "Track not found in playlist, unable to remove"

    def update_total(self):
        self.total = len(self.tracks)

    def __eq__(self, other):
        if isinstance(other, SpotifyPlaylist):
            return (self.playlist_id == other.playlist_id and
                    self.name == other.name and
                    self.tracks == other.tracks)
        return False