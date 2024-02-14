from src.classes.spotify_playlist import SpotifyPlaylist
from src.classes.spotify_track import SpotifyTrack
from pprint import pprint

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
            track_dict = {
                'track_id': item['track']['id'],
                'name': item['track']['name'],
                'album': item['track']['album']['name'],
                'artist': item['track']["artists"]["name"],
                'duration': item['track']["duration_ms"],
                'popularity': item['track']['popularity'],
                'release_date': item['track']['album']['release_date']
            }

        track = SpotifyTrack.from_dict(track_dict)
        tracks.add(track)
        return playlist