import tkinter as tk
from tkinter import ttk, messagebox


# === RECORD / TIPE DATA LAGU ===

class Song:
    def __init__(self, song_id, title, artist, album, year, genre):
        self.id = song_id
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"{self.id} - {self.title} ({self.artist})"


# === LIBRARY - SLL ===

class SLLNode:
    def __init__(self, song: Song):
        self.song = song
        self.next = None


class SongLibrarySLL:
    def __init__(self):
        self.head = None

    def add_song(self, song: Song):
        node = SLLNode(song)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def find_by_id(self, song_id):
        cur = self.head
        while cur:
            if cur.song.id == song_id:
                return cur.song
            cur = cur.next
        return None

    def update_song(self, song_id, new_song: Song):
        cur = self.head
        while cur:
            if cur.song.id == song_id:
                cur.song = new_song
                return True
            cur = cur.next
        return False

    def delete_song(self, song_id):
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
        result = []
        cur = self.head
        while cur:
            result.append(cur.song)
            cur = cur.next
        return result


# === PLAYLIST - DLL ===

class DLLNode:
    def __init__(self, song: Song):
        self.song = song
        self.prev = None
        self.next = None


class PlaylistDLL:
    # Playlist: Doubly Linked List, bisa next/prev.
    def __init__(self, name="Default Playlist"):
        self.name = name
        self.head = None
        self.tail = None
        self.current = None

    def append(self, song: Song):
        node = DLLNode(song)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove(self, song_id):
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
        result = []
        cur = self.head
        while cur:
            result.append(cur.song)
            cur = cur.next
        return result

    def set_current_by_index(self, index):
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
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.song
        return None

    def prev_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.song
        return None


# === RIWAYAT - STACK ===

class StackNode:
    def __init__(self, song: Song, next_node=None):
        self.song = song
        self.next = next_node


class PlaybackHistoryStack:
    def __init__(self):
        self.top = None

    def push(self, song: Song):
        self.top = StackNode(song, self.top)

    def pop(self):
        if not self.top:
            return None
        song = self.top.song
        self.top = self.top.next
        return song


# === UP NEXT - QUEUE ===

class QueueNode:
    def __init__(self, song: Song):
        self.song = song
        self.next = None


class UpNextQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, song: Song):
        node = QueueNode(song)
        if not self.rear:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front:
            return None
        node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return node.song

    def is_empty(self):
        return self.front is None


# === ARTIST -> LAGU - MLL ===

class ArtistSongNode:
    def __init__(self, song: Song):
        self.song = song
        self.next_song = None


class ArtistNode:
    def __init__(self, artist_name):
        self.artist_name = artist_name
        self.first_song = None
        self.next_artist = None


class ArtistMultiLinkedList:
    def __init__(self):
        self.head_artist = None

    def add_song(self, song: Song):
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


# === BST PENCARIAN JUDUL - TREE ===

class TreeNode:
    def __init__(self, key, song: Song):
        self.key = key.lower()
        self.song = song
        self.left = None
        self.right = None


class SongBST:
    def __init__(self):
        self.root = None

    def insert(self, song: Song):
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


# === LAGU MIRIP - GRAPH ===

class SongGraph:
    def __init__(self):
        self.adj = {}

    def add_song(self, song: Song):
        if song.id not in self.adj:
            self.adj[song.id] = set()

    def add_similarity(self, song1: Song, song2: Song):
        self.add_song(song1)
        self.add_song(song2)
        self.adj[song1.id].add(song2.id)
        self.adj[song2.id].add(song1.id)

    def get_similar(self, song_id):
        return list(self.adj.get(song_id, []))


# === CONTROLLER ===

class MusicPlayerController:
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

    # ----- Admin -----

    def add_song_to_library(self, song: Song):
        if self.library.find_by_id(song.id):
            raise ValueError("ID lagu sudah digunakan.")
        self.library.add_song(song)
        self.artists.add_song(song)
        self.search_tree.insert(song)
        self.graph.add_song(song)

        # buat edge lagu mirip (artist / genre sama)
        for s in self.library.to_list():
            if s.id == song.id:
                continue
            if s.artist == song.artist or s.genre == song.genre:
                self.graph.add_similarity(song, s)

    def update_song_in_library(self, song_id, new_song: Song):
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

    # ----- User -----

    def get_all_songs(self):
        return self.library.to_list()

    def search_song_by_title(self, title):
        return self.search_tree.search(title)

    def add_to_playlist(self, song_id):
        song = self.library.find_by_id(song_id)
        if not song:
            raise ValueError("Lagu tidak ditemukan.")
        self.playlist.append(song)

    def remove_from_playlist(self, song_id):
        if not self.playlist.remove(song_id):
            raise ValueError("Lagu tidak ada di playlist.")

    def play_song(self, song: Song, from_playlist=False):
        if not song:
            return None
        if self.current_song:
            self.history.push(self.current_song)
        self.current_song = song
        self.in_playlist_mode = from_playlist
        return song

    def stop_song(self):
        self.current_song = None

    def play_next(self):
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
        if self.in_playlist_mode and self.playlist.current:
            prev_song = self.playlist.prev_song()
            if prev_song:
                return self.play_song(prev_song, True)
        prev = self.history.pop()
        if prev:
            return self.play_song(prev, False)
        return None


# === GUI - TEMA & WARNA ===

class MusicPlayerGUI:
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
        self.library_listbox.delete(0, tk.END)
        for song in self.controller.get_all_songs():
            self.library_listbox.insert(tk.END, str(song))
        self.refresh_user_library_list()

    def refresh_user_library_list(self):
        self.user_library_listbox.delete(0, tk.END)
        for song in self.controller.get_all_songs():
            self.user_library_listbox.insert(tk.END, str(song))

    def refresh_playlist_list(self):
        self.playlist_listbox.delete(0, tk.END)
        for song in self.controller.playlist.to_list():
            self.playlist_listbox.insert(tk.END, str(song))

    def set_now_playing(self, song: Song):
        if song:
            self.now_playing_var.set(f"▶ {song.title} - {song.artist}")
        else:
            self.now_playing_var.set("🎵 Tidak ada lagu yang diputar.")

    # ---------- Admin Events ----------

    def on_add_song(self):
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
        selection = self.playlist_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Pilih lagu di playlist.")
            return
        index = selection[0]
        song = self.controller.playlist.set_current_by_index(index)
        played = self.controller.play_song(song, from_playlist=True)
        self.set_now_playing(played)

    def on_stop(self):
        self.controller.stop_song()
        self.set_now_playing(None)
        messagebox.showinfo("Info", "Lagu dihentikan (stop).")

    def on_next(self):
        song = self.controller.play_next()
        self.set_now_playing(song)

    def on_prev(self):
        song = self.controller.play_prev()
        self.set_now_playing(song)


# === MAIN ===

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerGUI(root)
    root.mainloop()
