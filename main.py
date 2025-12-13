"""
Music Player Application
Main entry point for the music player application.
"""

import tkinter as tk
from music_player.gui import MusicPlayerGUI


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerGUI(root)
    root.mainloop()
