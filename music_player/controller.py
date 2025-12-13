"""
Music Player Controller
Contains the main controller logic for managing the music player.
"""

from .models import Song
from .data_structures import (
    SongLibrarySLL,
    PlaylistDLL,
    PlaybackHistoryStack,
    UpNextQueue,
    ArtistMultiLinkedList,
    SongBST,
    SongGraph
)


class MusicPlayerController:
    """Controller for managing music player operations."""
    
    def __init__(self):
        self.library = SongLibrarySLL()
        self.playlist = PlaylistDLL()
        self.history = PlaybackHistoryStack()
        self.up_next = UpNextQueue()
        self.artists = ArtistMultiLinkedList()
        self.search_tree = SongBST()
        self.graph = SongGraph()

        self.current_song = None
        self.in_playlist_mode = False

    # ----- Admin Functions -----

    def add_song_to_library(self, song: Song):
        """Add a new song to the library."""
        if self.library.find_by_id(song.id):
            raise ValueError("ID lagu sudah digunakan.")
        self.library.add_song(song)
        self.artists.add_song(song)
        self.search_tree.insert(song)
        self.graph.add_song(song)

        # Create similarity edges (same artist or genre)
        for s in self.library.to_list():
            if s.id == song.id:
                continue
            if s.artist == song.artist or s.genre == song.genre:
                self.graph.add_similarity(song, s)

    def update_song_in_library(self, song_id, new_song: Song):
        """Update an existing song in the library."""
        old_song = self.library.find_by_id(song_id)
        if not old_song:
            raise ValueError("Lagu tidak ditemukan.")
        self.artists.remove_song(old_song)
        self.graph = SongGraph()
        self.search_tree = SongBST()
        self.library.update_song(song_id, new_song)
        for s in self.library.to_list():
            self.artists.add_song(s)
            self.search_tree.insert(s)
        songs = self.library.to_list()
        for i in range(len(songs)):
            for j in range(i + 1, len(songs)):
                s1, s2 = songs[i], songs[j]
                if s1.artist == s2.artist or s1.genre == s2.genre:
                    self.graph.add_similarity(s1, s2)

    def delete_song_from_library(self, song_id):
        """Delete a song from the library."""
        song = self.library.delete_song(song_id)
        if not song:
            raise ValueError("Lagu tidak ditemukan.")
        self.artists.remove_song(song)
        self.playlist.remove(song_id)
        self.search_tree = SongBST()
        self.graph = SongGraph()
        for s in self.library.to_list():
            self.search_tree.insert(s)
        songs = self.library.to_list()
        for i in range(len(songs)):
            for j in range(i + 1, len(songs)):
                s1, s2 = songs[i], songs[j]
                if s1.artist == s2.artist or s1.genre == s2.genre:
                    self.graph.add_similarity(s1, s2)

    # ----- User Functions -----

    def get_all_songs(self):
        """Get all songs from the library."""
        return self.library.to_list()

    def search_song_by_title(self, title):
        """Search for a song by title using BST."""
        return self.search_tree.search(title)

    def add_to_playlist(self, song_id):
        """Add a song to the playlist."""
        song = self.library.find_by_id(song_id)
        if not song:
            raise ValueError("Lagu tidak ditemukan.")
        self.playlist.append(song)

    def remove_from_playlist(self, song_id):
        """Remove a song from the playlist."""
        if not self.playlist.remove(song_id):
            raise ValueError("Lagu tidak ada di playlist.")

    def play_song(self, song: Song, from_playlist=False):
        """Play a song."""
        if not song:
            return None
        if self.current_song:
            self.history.push(self.current_song)
        self.current_song = song
        self.in_playlist_mode = from_playlist
        return song

    def stop_song(self):
        """Stop the current song."""
        self.current_song = None

    def play_next(self):
        """Play the next song."""
        if self.in_playlist_mode and self.playlist.current:
            next_song = self.playlist.next_song()
            if next_song:
                return self.play_song(next_song, True)

        if not self.up_next.is_empty():
            song = self.up_next.dequeue()
            return self.play_song(song, False)

        if self.current_song:
            similar_ids = self.graph.get_similar(self.current_song.id)
            for sid in similar_ids:
                s = self.library.find_by_id(sid)
                if s:
                    return self.play_song(s, False)

        songs = self.library.to_list()
        if songs:
            return self.play_song(songs[0], False)
        return None

    def play_prev(self):
        """Play the previous song."""
        if self.in_playlist_mode and self.playlist.current:
            prev_song = self.playlist.prev_song()
            if prev_song:
                return self.play_song(prev_song, True)
        prev = self.history.pop()
        if prev:
            return self.play_song(prev, False)
        return None
