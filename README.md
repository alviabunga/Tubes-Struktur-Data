# Music Player - Struktur Data

🎵 **Aplikasi Pemutar Musik dengan Implementasi Berbagai Struktur Data**

## 📖 Deskripsi Proyek

Music Player adalah aplikasi desktop berbasis Python yang mendemonstrasikan penggunaan berbagai struktur data dalam konteks nyata. Aplikasi ini memanfaatkan 7 jenis struktur data berbeda untuk mengelola perpustakaan musik, playlist, riwayat pemutaran, dan fitur-fitur lainnya.

## ✨ Fitur Utama

### Admin Features
- ➕ **Tambah Lagu**: Menambahkan lagu baru ke library
- ✏️ **Update Lagu**: Mengubah informasi lagu yang sudah ada
- 🗑️ **Hapus Lagu**: Menghapus lagu dari library
- 📂 **Kelola Library**: Melihat semua lagu dalam library

### User Features
- 🔍 **Pencarian Cepat**: Cari lagu berdasarkan judul (Binary Search Tree)
- 📻 **Playlist Management**: Tambah/hapus lagu dari playlist
- ▶️ **Playback Control**: Play, Stop, Next, Previous
- 🎵 **Auto-Recommendation**: Sistem rekomendasi lagu mirip berdasarkan artist/genre
- 📊 **History Tracking**: Lacak riwayat pemutaran

## 🏗️ Struktur Data yang Digunakan

| Struktur Data | Implementasi | Fungsi |
|---------------|--------------|--------|
| **Single Linked List (SLL)** | `SongLibrarySLL` | Menyimpan library lagu |
| **Doubly Linked List (DLL)** | `PlaylistDLL` | Playlist dengan navigasi maju-mundur |
| **Stack** | `PlaybackHistoryStack` | Riwayat pemutaran (LIFO) |
| **Queue** | `UpNextQueue` | Antrian lagu berikutnya (FIFO) |
| **Multi-Linked List** | `ArtistMultiLinkedList` | Pengelompokan lagu per artist |
| **Binary Search Tree (BST)** | `SongBST` | Pencarian lagu berdasarkan judul |
| **Graph** | `SongGraph` | Relasi kemiripan antar lagu |

## 📁 Struktur Folder

```
c:\Project\StrukDat\
├── music_player/              # Package utama
│   ├── __init__.py           # Package initializer
│   ├── models.py             # Data model (Song class)
│   ├── controller.py         # Controller logic
│   ├── gui.py                # Graphical User Interface
│   ├── utils.py              # Helper functions
│   └── data_structures/      # Data structures package
│       ├── __init__.py
│       ├── linked_lists.py   # SLL, DLL, Multi-Linked List
│       ├── stack_queue.py    # Stack dan Queue
│       ├── tree.py           # Binary Search Tree
│       └── graph.py          # Graph
├── main.py                   # Entry point aplikasi
├── music-player.py           # Original monolithic file (reference)
├── README.md                 # Dokumentasi (file ini)
└── CHANGELOG.md              # Log perubahan
```

## 🚀 Cara Menjalankan

### Prerequisites
- Python 3.7 atau lebih tinggi
- Tkinter (biasanya sudah terinstall dengan Python)

### Langkah-langkah

1. **Clone atau download repository**
   ```bash
   cd c:\Project\StrukDat
   ```

2. **Jalankan aplikasi**
   ```bash
   python main.py
   ```

3. **Aplikasi akan terbuka dengan GUI**

## 📚 Penjelasan Modul

### `models.py`
Berisi class `Song` yang merepresentasikan data lagu dengan atribut:
- ID (unique identifier)
- Title (judul lagu)
- Artist (nama artis)
- Album (nama album)
- Year (tahun rilis)
- Genre (genre musik)

### `data_structures/`

#### `linked_lists.py`
- **SongLibrarySLL**: Implementasi Single Linked List untuk library lagu
  - `add_song()`: Tambah lagu di head
  - `find_by_id()`: Cari lagu berdasarkan ID
  - `update_song()`: Update informasi lagu
  - `delete_song()`: Hapus lagu dari list
  - `to_list()`: Konversi ke Python list

- **PlaylistDLL**: Implementasi Doubly Linked List untuk playlist
  - `append()`: Tambah lagu di tail
  - `remove()`: Hapus lagu dari playlist
  - `next_song()`: Navigasi ke lagu berikutnya
  - `prev_song()`: Navigasi ke lagu sebelumnya
  - `set_current_by_index()`: Set lagu aktif

- **ArtistMultiLinkedList**: Multi-level linked list
  - Level 1: Artist nodes (linked list of artists)
  - Level 2: Song nodes per artist (linked list of songs)

#### `stack_queue.py`
- **PlaybackHistoryStack**: Stack untuk riwayat pemutaran
  - `push()`: Tambah lagu ke history
  - `pop()`: Ambil lagu terakhir dari history

- **UpNextQueue**: Queue untuk antrian lagu
  - `enqueue()`: Tambah lagu ke antrian
  - `dequeue()`: Ambil lagu dari depan antrian
  - `is_empty()`: Cek apakah queue kosong

#### `tree.py`
- **SongBST**: Binary Search Tree untuk pencarian judul
  - `insert()`: Insert lagu ke BST (sorted by title)
  - `search()`: Cari lagu dengan kompleksitas O(log n)

#### `graph.py`
- **SongGraph**: Graph untuk relasi kemiripan lagu
  - `add_song()`: Tambah node lagu
  - `add_similarity()`: Tambah edge kemiripan
  - `get_similar()`: Dapatkan lagu-lagu mirip

### `controller.py`
**MusicPlayerController** - Orchestrates semua data structures:

**Admin Functions:**
- `add_song_to_library()`: Tambah lagu ke semua struktur data
- `update_song_in_library()`: Update lagu dan rebuild indexes
- `delete_song_from_library()`: Hapus lagu dari semua struktur

**User Functions:**
- `get_all_songs()`: Ambil semua lagu
- `search_song_by_title()`: Cari lagu via BST
- `add_to_playlist()`: Tambah ke playlist
- `play_song()`: Putar lagu
- `play_next()`: Putar lagu berikutnya (logic pintar)
- `play_prev()`: Putar lagu sebelumnya

### `gui.py`
**MusicPlayerGUI** - Interface pengguna dengan Tkinter:
- Tab Admin untuk CRUD operations
- Tab User untuk playback dan playlist management
- Visual styling dengan warna-warna cerah
- Event handlers untuk semua interaksi user

## 🎯 Workflow Penggunaan

### Sebagai Admin
1. Buka tab "Admin 🎚️"
2. Isi form dengan informasi lagu (ID, Judul, Artist, Album, Tahun, Genre)
3. Klik "➕ Tambah Lagu" untuk menambah
4. Untuk update: isi ID dan informasi baru, klik "✏️ Update Lagu"
5. Untuk hapus: isi ID, klik "🗑 Hapus Lagu"

### Sebagai User
1. Buka tab "User 🎧"
2. **Cari Lagu**: Masukkan judul di search box, klik "Cari"
3. **Buat Playlist**:
   - Pilih lagu dari Library
   - Klik "➕ ke Playlist"
4. **Putar Lagu**:
   - Dari Library: Pilih lagu, klik "▶ Play dari Library"
   - Dari Playlist: Pilih lagu, klik "🎼 Play dari Playlist"
5. **Kontrol Pemutaran**:
   - "⏭ Next": Lagu berikutnya (otomatis rekomendasikan lagu mirip)
   - "⏮ Prev": Lagu sebelumnya (dari history)
   - "⏹ Stop": Berhenti

## 🔄 Logic Pemutaran

### Next Song Logic
1. Jika dalam mode playlist → ambil lagu berikutnya dari playlist (DLL)
2. Jika ada queue → ambil dari queue (FIFO)
3. Jika tidak ada → rekomendasikan lagu mirip via Graph
4. Fallback → lagu pertama di library

### Previous Song Logic
1. Jika dalam mode playlist → ambil lagu sebelumnya dari playlist (DLL)
2. Jika tidak → ambil dari history (Stack - LIFO)

## 💡 Keunggulan Modular Structure

### Sebelum (Monolithic)
- ❌ 877 baris dalam 1 file
- ❌ Sulit maintenance
- ❌ Kode sulit dibaca
- ❌ Testing sulit dilakukan

### Sesudah (Modular)
- ✅ Terorganisir dalam package terstruktur
- ✅ Separation of concerns jelas
- ✅ Mudah di-maintain dan extend
- ✅ Setiap modul fokus pada tanggung jawabnya
- ✅ Reusable components
- ✅ Easier testing dan debugging

## 🧪 Testing

Untuk memverifikasi aplikasi bekerja dengan baik:

1. **Test Admin Functions**:
   - Tambah lagu dengan ID unik
   - Update lagu yang sudah ada
   - Hapus lagu
   - Verifikasi library list ter-update

2. **Test User Functions**:
   - Cari lagu yang sudah ditambahkan
   - Buat playlist dengan beberapa lagu
   - Putar lagu dan test navigasi next/prev
   - Test remove dari playlist

3. **Test Data Structures**:
   - SLL: Library tetap konsisten setelah add/delete
   - DLL: Navigasi playlist maju-mundur
   - Stack: History tracking yang benar
   - BST: Pencarian case-insensitive
   - Graph: Rekomendasi lagu mirip

## 🛠️ Pengembangan Lebih Lanjut

Ide untuk fitur tambahan:
- 💾 Persistence (save/load library ke file)
- 🎨 Theme customization
- 📊 Analytics dan statistics
- 🔊 Audio playback integration
- 🎲 Shuffle mode
- 🔁 Repeat mode
- 📝 Lyrics display
- ⭐ Rating system
- 🔖 Multiple playlists

## 📝 Lisensi

Proyek ini dibuat untuk tujuan edukasi dalam mempelajari struktur data.

## 👨‍💻 Kontak

Untuk pertanyaan atau saran, silakan hubungi developer.

---

**Happy Coding! 🎵🎧**
