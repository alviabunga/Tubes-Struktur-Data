"""
Binary Search Tree
Contains BST for efficient song title search.
"""

from ..models import Song


# === SONG SEARCH - BINARY SEARCH TREE ===

class TreeNode:
    """Node for Binary Search Tree."""
    
    def __init__(self, key, song: Song):
        self.key = key.lower()
        self.song = song
        self.left = None
        self.right = None


class SongBST:
    """Binary Search Tree for searching songs by title."""
    
    def __init__(self):
        self.root = None

    def insert(self, song: Song):
        """Insert a song into the BST."""
        def _insert(node, key, song):
            if not node:
                return TreeNode(key, song)
            if key < node.key:
                node.left = _insert(node.left, key, song)
            elif key > node.key:
                node.right = _insert(node.right, key, song)
            else:
                node.song = song
            return node
        self.root = _insert(self.root, song.title.lower(), song)

    def search(self, title):
        """Search for a song by title."""
        key = title.lower()
        cur = self.root
        while cur:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.song
        return None
