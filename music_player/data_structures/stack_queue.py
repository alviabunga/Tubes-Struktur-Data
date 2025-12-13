"""
Stack and Queue Data Structures
Contains Stack for playback history and Queue for up-next songs.
"""

from ..models import Song


# === PLAYBACK HISTORY - STACK ===

class StackNode:
    """Node for Stack."""
    
    def __init__(self, song: Song, next_node=None):
        self.song = song
        self.next = next_node


class PlaybackHistoryStack:
    """Stack for tracking playback history."""
    
    def __init__(self):
        self.top = None

    def push(self, song: Song):
        """Push a song onto the history stack."""
        self.top = StackNode(song, self.top)

    def pop(self):
        """Pop a song from the history stack."""
        if not self.top:
            return None
        song = self.top.song
        self.top = self.top.next
        return song


# === UP NEXT - QUEUE ===

class QueueNode:
    """Node for Queue."""
    
    def __init__(self, song: Song):
        self.song = song
        self.next = None


class UpNextQueue:
    """Queue for managing up-next songs."""
    
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, song: Song):
        """Add a song to the up-next queue."""
        node = QueueNode(song)
        if not self.rear:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """Remove and return the next song from the queue."""
        if not self.front:
            return None
        node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return node.song

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None
