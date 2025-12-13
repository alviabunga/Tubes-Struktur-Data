"""
Data Structures Package
Contains implementations of various data structures used in the music player.
"""

from .linked_lists import SLLNode, SongLibrarySLL, DLLNode, PlaylistDLL
from .linked_lists import ArtistSongNode, ArtistNode, ArtistMultiLinkedList
from .stack_queue import StackNode, PlaybackHistoryStack, QueueNode, UpNextQueue
from .tree import TreeNode, SongBST
from .graph import SongGraph

__all__ = [
    'SLLNode', 'SongLibrarySLL',
    'DLLNode', 'PlaylistDLL',
    'ArtistSongNode', 'ArtistNode', 'ArtistMultiLinkedList',
    'StackNode', 'PlaybackHistoryStack',
    'QueueNode', 'UpNextQueue',
    'TreeNode', 'SongBST',
    'SongGraph'
]
