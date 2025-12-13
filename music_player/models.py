"""
Data Models
Contains the Song class representing a music track.
"""


class Song:
    """Represents a song with metadata."""
    
    def __init__(self, song_id, title, artist, album, year, genre):
        self.id = song_id
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"{self.id} - {self.title} ({self.artist})"
