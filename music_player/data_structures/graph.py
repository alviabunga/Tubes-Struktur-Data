"""
Graph Data Structure
Contains graph for managing similar songs based on artist/genre.
"""

from ..models import Song


# === SIMILAR SONGS - GRAPH ===

class SongGraph:
    """Graph for tracking similar songs."""
    
    def __init__(self):
        self.adj = {}

    def add_song(self, song: Song):
        """Add a song node to the graph."""
        if song.id not in self.adj:
            self.adj[song.id] = set()

    def add_similarity(self, song1: Song, song2: Song):
        """Add a similarity edge between two songs."""
        self.add_song(song1)
        self.add_song(song2)
        self.adj[song1.id].add(song2.id)
        self.adj[song2.id].add(song1.id)

    def get_similar(self, song_id):
        """Get list of similar song IDs."""
        return list(self.adj.get(song_id, []))
