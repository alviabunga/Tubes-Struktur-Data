"""
Music Player GUI
Contains the graphical user interface for the music player.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from .models import Song
from .controller import MusicPlayerController


class MusicPlayerGUI:
    """Graphical User Interface for the Music Player."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🎧 Pemutar Musik - Struktur Data")
        self.root.geometry("1100x600")
        self.root.configure(bg="#fff7ed")  # krem terang

        # styling ttk: warna-warni
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Main.TFrame", background="#fff7ed")
        style.configure("Card.TLabelframe",
                        background="#fff7ed",
                        foreground="#1f2937")
        style.configure("Card.TLabelframe.Label",
                        background="#fff7ed",
                        foreground="#1f2937",
                        font=("Segoe UI", 10, "bold"))
        style.configure("TLabel", background="#fff7ed", foreground="#1f2937")
        style.configure("TNotebook", background="#fff7ed", borderwidth=0)
        style.configure("TNotebook.Tab",
                        padding=(12, 4),
                        font=("Segoe UI", 10, "bold"),
                        background="#fed7e2")
        style.map("TNotebook.Tab",
                  background=[("selected", "#fb7185")],
                  foreground=[("selected", "white")])

        style.configure("Color.TButton",
                        font=("Segoe UI", 9, "bold"),
                        padding=5,
                        background="#22c55e",
                        foreground="white")
        style.map("Color.TButton",
                  background=[("active", "#16a34a")])

        self.controller = MusicPlayerController()

        self.create_widgets()

    def create_widgets(self):
        """Create all GUI widgets."""
        # banner colorful
        banner = tk.Frame(self.root, bg="#fb7185", height=60)
        banner.pack(fill="x", side="top")

        title = tk.Label(
            banner,
            text="🎵  Music Player  🎵",
            fg="#fef9c3",
            bg="#fb7185",
            font=("Segoe UI", 16, "bold")
        )
        title.pack(side="left", padx=20)

        subtitle = tk.Label(
            banner,
            text="SLL • DLL • Stack • Queue • Multi Linked List • Tree • Graph",
            fg="#fefce8",
            bg="#fb7185",
            font=("Segoe UI", 9)
        )
        subtitle.pack(side="left", padx=10)

        notebook_frame = ttk.Frame(self.root, style="Main.TFrame")
        notebook_frame.pack(fill="both", expand=True)

        notebook = ttk.Notebook(notebook_frame)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.admin_frame = ttk.Frame(notebook, padding=15, style="Main.TFrame")
        self.user_frame = ttk.Frame(notebook, padding=15, style="Main.TFrame")

        notebook.add(self.admin_frame, text="Admin 🎚️")
        notebook.add(self.user_frame, text="User 🎧")

        self.build_admin_tab()
        self.build_user_tab()

    # ---------- Admin Tab ----------

    def build_admin_tab(self):
        """Build the admin tab interface."""
        f = self.admin_frame

        admin_card = ttk.Labelframe(
            f, text="🎼 Kelola Library Lagu", padding=15, style="Card.TLabelframe"
        )
        admin_card.grid(row=0, column=0, sticky="nsew")

        labels = ["ID", "Judul", "Artist", "Album", "Tahun", "Genre"]
        self.admin_entries = {}
        for i, lbl in enumerate(labels):
            ttk.Label(admin_card, text=lbl, font=("Segoe UI", 10)).grid(
                row=i, column=0, sticky="w", pady=3
            )
            ent = ttk.Entry(admin_card, width=40)
            ent.grid(row=i, column=1, sticky="w", pady=3, padx=5)
            self.admin_entries[lbl.lower()] = ent

        btn_frame = ttk.Frame(admin_card, style="Main.TFrame")
        btn_frame.grid(row=6, column=0, columnspan=2, pady=(10, 5))

        ttk.Button(btn_frame, text="➕ Tambah Lagu",
                   style="Color.TButton",
                   command=self.on_add_song).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="✏️ Update Lagu",
                   style="Color.TButton",
                   command=self.on_update_song).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="🗑 Hapus Lagu",
                   style="Color.TButton",
                   command=self.on_delete_song).grid(row=0, column=2, padx=5)
        ttk.Button(btn_frame, text="📂 Muat Ulang Library",
                   style="Color.TButton",
                   command=self.refresh_library_list).grid(row=0, column=3, padx=5)

        list_card = ttk.Labelframe(
            f, text="Library Lagu", padding=10, style="Card.TLabelframe"
        )
        list_card.grid(row=1, column=0, sticky="nsew", pady=(15, 0))
        f.rowconfigure(1, weight=1)
        f.columnconfigure(0, weight=1)

        self.library_listbox = tk.Listbox(
            list_card,
            width=100,
            height=10,
            bg="#f0f9ff",
            fg="#111827",
            selectbackground="#bfdbfe",
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="#60a5fa",
            font=("Consolas", 9)
        )
        self.library_listbox.pack(fill="both", expand=True)

    # ---------- User Tab ----------

    def build_user_tab(self):
        """Build the user tab interface."""
        f = self.user_frame

        top_frame = ttk.Frame(f, style="Main.TFrame")
        top_frame.pack(fill="x")

        search_frame = ttk.Labelframe(
            top_frame, text="🔍 Cari Lagu (BST Judul)", padding=10, style="Card.TLabelframe"
        )
        search_frame.pack(side="left", padx=(0, 10), pady=(0, 10))

        ttk.Label(search_frame, text="Judul:").pack(side="left")
        self.search_entry = ttk.Entry(search_frame, width=30)
        self.search_entry.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Cari",
                   style="Color.TButton",
                   command=self.on_search_song).pack(side="left")

        np_frame = ttk.Labelframe(
            top_frame, text="Now Playing", padding=10, style="Card.TLabelframe"
        )
        np_frame.pack(side="left", padx=10, pady=(0, 10), fill="x", expand=True)

        self.now_playing_var = tk.StringVar()
        self.now_playing_var.set("🎵 Tidak ada lagu yang diputar.")
        self.now_playing_label = ttk.Label(
            np_frame,
            textvariable=self.now_playing_var,
            font=("Segoe UI", 11, "bold"),
            foreground="#be123c"
        )
        self.now_playing_label.pack(anchor="w")

        mid_frame = ttk.Frame(f, style="Main.TFrame")
        mid_frame.pack(fill="both", expand=True)

        # Library
        lib_frame = ttk.Labelframe(
            mid_frame, text="🎶 Library", padding=10, style="Card.TLabelframe"
        )
        lib_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        self.user_library_listbox = tk.Listbox(
            lib_frame,
            width=40,
            height=15,
            bg="#ecfeff",
            fg="#0f172a",
            selectbackground="#a5f3fc",
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="#06b6d4",
            font=("Consolas", 9)
        )
        self.user_library_listbox.pack(fill="both", expand=True)

        # Playlist
        playlist_frame = ttk.Labelframe(
            mid_frame, text="📻 Playlist", padding=10,
            style="Card.TLabelframe"
        )
        playlist_frame.pack(side="left", fill="both", expand=True)

        self.playlist_listbox = tk.Listbox(
            playlist_frame,
            width=40,
            height=15,
            bg="#fef9c3",
            fg="#0f172a",
            selectbackground="#fde68a",
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="#facc15",
            font=("Consolas", 9)
        )
        self.playlist_listbox.pack(fill="both", expand=True)

        # Control buttons
        btn2_frame = ttk.Labelframe(
            f, text="🎛 Kontrol Pemutar", padding=10, style="Card.TLabelframe"
        )
        btn2_frame.pack(fill="x", pady=(10, 0))

        ttk.Button(btn2_frame, text="➕ ke Playlist",
                   style="Color.TButton",
                   command=self.on_add_to_playlist).pack(side="left", padx=4)
        ttk.Button(btn2_frame, text="🗑 dari Playlist",
                   style="Color.TButton",
                   command=self.on_remove_from_playlist).pack(side="left", padx=4)
        ttk.Button(btn2_frame, text="▶ Play dari Library",
                   style="Color.TButton",
                   command=self.on_play_from_library).pack(side="left", padx=4)
        ttk.Button(btn2_frame, text="🎼 Play dari Playlist",
                   style="Color.TButton",
                   command=self.on_play_from_playlist).pack(side="left", padx=4)
        ttk.Button(btn2_frame, text="⏹ Stop",
                   style="Color.TButton",
                   command=self.on_stop).pack(side="left", padx=4)
        ttk.Button(btn2_frame, text="⏮ Prev",
                   style="Color.TButton",
                   command=self.on_prev).pack(side="left", padx=4)
        ttk.Button(btn2_frame, text="⏭ Next",
                   style="Color.TButton",
                   command=self.on_next).pack(side="left", padx=4)

        self.refresh_library_list()
        self.refresh_user_library_list()
        self.refresh_playlist_list()

    # ---------- Helpers ----------

    def get_admin_song_from_entries(self):
        """Get song data from admin entry fields."""
        try:
            song_id = self.admin_entries["id"].get().strip()
            title = self.admin_entries["judul"].get().strip()
            artist = self.admin_entries["artist"].get().strip()
            album = self.admin_entries["album"].get().strip()
            year = self.admin_entries["tahun"].get().strip()
            genre = self.admin_entries["genre"].get().strip()
            if not song_id or not title:
                raise ValueError("ID dan Judul wajib diisi.")
            return Song(song_id, title, artist, album, year, genre)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return None

    def refresh_library_list(self):
        """Refresh the library listbox."""
        self.library_listbox.delete(0, tk.END)
        for song in self.controller.get_all_songs():
            self.library_listbox.insert(tk.END, str(song))
        self.refresh_user_library_list()

    def refresh_user_library_list(self):
        """Refresh the user library listbox."""
        self.user_library_listbox.delete(0, tk.END)
        for song in self.controller.get_all_songs():
            self.user_library_listbox.insert(tk.END, str(song))

    def refresh_playlist_list(self):
        """Refresh the playlist listbox."""
        self.playlist_listbox.delete(0, tk.END)
        for song in self.controller.playlist.to_list():
            self.playlist_listbox.insert(tk.END, str(song))

    def set_now_playing(self, song: Song):
        """Update the now playing display."""
        if song:
            self.now_playing_var.set(f"▶ {song.title} - {song.artist}")
        else:
            self.now_playing_var.set("🎵 Tidak ada lagu yang diputar.")

    # ---------- Admin Events ----------

    def on_add_song(self):
        """Handle add song button click."""
        song = self.get_admin_song_from_entries()
        if not song:
            return
        try:
            self.controller.add_song_to_library(song)
            messagebox.showinfo("Sukses", "Lagu berhasil ditambahkan.")
            self.refresh_library_list()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_update_song(self):
        """Handle update song button click."""
        song = self.get_admin_song_from_entries()
        if not song:
            return
        try:
            self.controller.update_song_in_library(song.id, song)
            messagebox.showinfo("Sukses", "Lagu berhasil diupdate.")
            self.refresh_library_list()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_delete_song(self):
        """Handle delete song button click."""
        song_id = self.admin_entries["id"].get().strip()
        if not song_id:
            messagebox.showerror("Error", "Isi ID lagu yang akan dihapus.")
            return
        try:
            self.controller.delete_song_from_library(song_id)
            messagebox.showinfo("Sukses", "Lagu berhasil dihapus.")
            self.refresh_library_list()
            self.refresh_playlist_list()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------- User Events ----------

    def on_search_song(self):
        """Handle search song button click."""
        title = self.search_entry.get().strip()
        if not title:
            messagebox.showerror("Error", "Masukkan judul lagu.")
            return
        song = self.controller.search_song_by_title(title)
        if song:
            messagebox.showinfo("Hasil Cari", f"Ditemukan:\n{song}")
        else:
            messagebox.showinfo("Hasil Cari", "Lagu tidak ditemukan.")

    def on_add_to_playlist(self):
        """Handle add to playlist button click."""
        selection = self.user_library_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Pilih lagu dari library.")
            return
        index = selection[0]
        songs = self.controller.get_all_songs()
        if index < len(songs):
            song = songs[index]
            try:
                self.controller.add_to_playlist(song.id)
                self.refresh_playlist_list()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def on_remove_from_playlist(self):
        """Handle remove from playlist button click."""
        selection = self.playlist_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Pilih lagu di playlist.")
            return
        index = selection[0]
        songs = self.controller.playlist.to_list()
        if index < len(songs):
            song = songs[index]
            try:
                self.controller.remove_from_playlist(song.id)
                self.refresh_playlist_list()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def on_play_from_library(self):
        """Handle play from library button click."""
        selection = self.user_library_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Pilih lagu di library.")
            return
        index = selection[0]
        songs = self.controller.get_all_songs()
        if index < len(songs):
            song = songs[index]
            played = self.controller.play_song(song, from_playlist=False)
            self.set_now_playing(played)

    def on_play_from_playlist(self):
        """Handle play from playlist button click."""
        selection = self.playlist_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Pilih lagu di playlist.")
            return
        index = selection[0]
        song = self.controller.playlist.set_current_by_index(index)
        played = self.controller.play_song(song, from_playlist=True)
        self.set_now_playing(played)

    def on_stop(self):
        """Handle stop button click."""
        self.controller.stop_song()
        self.set_now_playing(None)
        messagebox.showinfo("Info", "Lagu dihentikan (stop).")

    def on_next(self):
        """Handle next button click."""
        song = self.controller.play_next()
        self.set_now_playing(song)

    def on_prev(self):
        """Handle previous button click."""
        song = self.controller.play_prev()
        self.set_now_playing(song)
