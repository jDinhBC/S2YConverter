from classes.spotify_playlist import SpotifyPlaylist
from classes.spotify_track import SpotifyTrack

class SpotifyParser:

    def __init__(self) -> None:
        pass

    # Spotify Data structure
    """
    {
        "id": "string",
        "name": "string",
        
        "tracks": {
        
            "total": int,
            "items": [
            
                "track": {
                
                    "album": {
                        "release_date": "0000-00"
                        "release_date_precision": "year"
                    },
                    
                    "artists": [
                        {
                            "id": "string",
                            "name": "string"
                        }
                    ],

                    "id": "string",
                    "name": "string",
                    "duration_ms": int,
                    "popularity": int,

                }
            ]
        }
    }
    """
    
    

    def spotifyPlaylistMapper(self, raw_data) -> SpotifyPlaylist():
        playlist = SpotifyPlaylist()
        playlist.name = raw_data['name']
        playlist.playlist_id = raw_data['id']
        tracks = set()

        for item in raw_data['tracks']['items']:
            track = SpotifyTrack()
            track.track_id = item['track']['id']
            track.name = item['track']['name']
            track.album = item['track']['album']['name']
            track.artist = item['track']["artists"]
            track.duration = item['track']["duration_ms"]
            track.popularity = item['track']['popularity']
            track.release_date = item['track']['album']['release_date']

            tracks.add(track)

        playlist.tracks = tracks
        return playlist