
class SpotifyTrack:

    def __init__(self, track_id, name, album, artist, duration, popularity, release_date):
        self.track_id = track_id
        self.name = name
        self.album = album
        self.artist = artist
        self.duration = duration
        self.popularity = popularity
        self.release_date = release_date

    @classmethod
    def from_dict(cls, track_dict):
        return cls(
            track_id=track_dict['track_id'],
            name=track_dict['name'],
            album=track_dict['album'],
            artist=track_dict['artist'],
            duration=track_dict['duration'],
            popularity=track_dict['popularity'],
            release_date=track_dict['release_date']
        )

    def __eq__(self, other):
        if isinstance(other, SpotifyTrack):
            return (self.track_id == other.track_id and
                    self.name == other.name and
                    self.album == other.album and
                    self.artist == other.artist and
                    self.duration == other.duration and
                    self.popularity == other.popularity and
                    self.release_date == other.release_date)
        return False

    def __hash__(self):
        # Convert each artist dictionary to a string
        artists_strings = [str(artist) for artist in self.artist]
        return hash((self.track_id, self.name, self.album, tuple(artists_strings), self.duration, self.popularity, self.release_date))