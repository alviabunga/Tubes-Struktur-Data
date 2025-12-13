"""
Linked List Data Structures
Contains Single Linked List, Doubly Linked List, and Multi-Linked List implementations.
"""

from ..models import Song


# === LIBRARY - SINGLE LINKED LIST ===

class SLLNode:
    """Node for Single Linked List."""
    
    def __init__(self, song: Song):
        self.song = song
        self.next = None


class SongLibrarySLL:
    """Single Linked List for managing the song library."""
    
    def __init__(self):
        self.head = None

    def add_song(self, song: Song):
        """Add a song to the library."""
        node = SLLNode(song)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def find_by_id(self, song_id):
        """Find a song by its ID."""
        cur = self.head
        while cur:
            if cur.song.id == song_id:
                return cur.song
            cur = cur.next
        return None

    def update_song(self, song_id, new_song: Song):
        """Update a song in the library."""
        cur = self.head
        while cur:
            if cur.song.id == song_id:
                cur.song = new_song
                return True
            cur = cur.next
        return False

    def delete_song(self, song_id):
        """Delete a song from the library."""
        cur = self.head
        prev = None
        while cur:
            if cur.song.id == song_id:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return cur.song
            prev = cur
            cur = cur.next
        return None

    def to_list(self):
        """Convert the linked list to a Python list."""
        result = []
        cur = self.head
        while cur:
            result.append(cur.song)
            cur = cur.next
        return result


# === PLAYLIST - DOUBLY LINKED LIST ===

class DLLNode:
    """Node for Doubly Linked List."""
    
    def __init__(self, song: Song):
        self.song = song
        self.prev = None
        self.next = None


class PlaylistDLL:
    """Doubly Linked List for playlist with forward/backward navigation."""
    
    def __init__(self, name="Default Playlist"):
        self.name = name
        self.head = None
        self.tail = None
        self.current = None

    def append(self, song: Song):
        """Append a song to the playlist."""
        node = DLLNode(song)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove(self, song_id):
        """Remove a song from the playlist."""
        cur = self.head
        while cur:
            if cur.song.id == song_id:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    self.tail = cur.prev
                if self.current == cur:
                    self.current = cur.next or cur.prev
                return True
            cur = cur.next
        return False

    def to_list(self):
        """Convert the doubly linked list to a Python list."""
        result = []
        cur = self.head
        while cur:
            result.append(cur.song)
            cur = cur.next
        return result

    def set_current_by_index(self, index):
        """Set the current song by index."""
        cur = self.head
        i = 0
        while cur:
            if i == index:
                self.current = cur
                return cur.song
            i += 1
            cur = cur.next
        return None

    def next_song(self):
        """Get the next song in the playlist."""
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.song
        return None

    def prev_song(self):
        """Get the previous song in the playlist."""
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.song
        return None


# === ARTIST -> SONGS - MULTI-LINKED LIST ===

class ArtistSongNode:
    """Node for songs within an artist's song list."""
    
    def __init__(self, song: Song):
        self.song = song
        self.next_song = None


class ArtistNode:
    """Node representing an artist with their songs."""
    
    def __init__(self, artist_name):
        self.artist_name = artist_name
        self.first_song = None
        self.next_artist = None


class ArtistMultiLinkedList:
    """Multi-Linked List for grouping songs by artist."""
    
    def __init__(self):
        self.head_artist = None

    def add_song(self, song: Song):
        """Add a song to an artist's song list."""
        cur_artist = self.head_artist
        prev_artist = None
        while cur_artist:
            if cur_artist.artist_name == song.artist:
                break
            prev_artist = cur_artist
            cur_artist = cur_artist.next_artist

        if not cur_artist:
            cur_artist = ArtistNode(song.artist)
            if not self.head_artist:
                self.head_artist = cur_artist
            else:
                prev_artist.next_artist = cur_artist

        new_song_node = ArtistSongNode(song)
        new_song_node.next_song = cur_artist.first_song
        cur_artist.first_song = new_song_node

    def remove_song(self, song: Song):
        """Remove a song from an artist's song list."""
        cur_artist = self.head_artist
        prev_artist = None
        while cur_artist:
            if cur_artist.artist_name == song.artist:
                cur_song = cur_artist.first_song
                prev_song = None
                while cur_song:
                    if cur_song.song.id == song.id:
                        if prev_song:
                            prev_song.next_song = cur_song.next_song
                        else:
                            cur_artist.first_song = cur_song.next_song
                        break
                    prev_song = cur_song
                    cur_song = cur_song.next_song
                if not cur_artist.first_song:
                    if prev_artist:
                        prev_artist.next_artist = cur_artist.next_artist
                    else:
                        self.head_artist = cur_artist.next_artist
                return
            prev_artist = cur_artist
            cur_artist = cur_artist.next_artist
