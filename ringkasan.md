# Ringkasan Belajar Python (Hari 1 - 5)

## Hari 1: Pengenalan dan Variabel
- **Fungsi Print & Input**: Menggunakan `print()` untuk menampilkan output ke layar dan `input("Teks: ")` untuk mengambil masukan dari pengguna.
- **Variabel**: Tempat menyimpan data. Contoh: `nama = "Daviano"`.

## Hari 2: Tipe Data
Tipe data dibagi menjadi dua kategori utama:
- **Tipe Data Primitif** (Hanya menyimpan satu nilai):
  - `Integer`: Bilangan bulat (contoh: 17).
  - `Float`: Bilangan desimal (contoh: 3.14).
  - `Boolean`: Nilai kebenaran (`True` atau `False`).
  - `String`: Teks/karakter (`"Halo"`).
- **Tipe Data Collection** (Menyimpan banyak nilai):
  - `List`: Berurutan, bisa diubah isi nilainya (`[1, 2, 3]`).
  - `Tuple`: Berurutan, TIDAK bisa diubah (`(1, 2, 3)`).
  - `Set`: Tidak berurutan, nilai unik/tidak ada duplikat (`{1, 2, 3}`).
  - `Dictionary`: Pasangan kunci dan nilai (`{"nama": "Daviano", "umur": 20}`).
- **Konversi Tipe Data**: Bisa menggunakan fungsi `int()`, `float()`, `str()`, `list()`, dsb untuk mengubah bentuk format data.

## Hari 3: Transformasi String
- **Kapitalisasi**: `.upper()` (huruf besar semua) dan `.lower()` (huruf kecil semua).
- **Menghapus Spasi/Karakter**: `.strip()` (kiri & kanan), `.lstrip()` (kiri), `.rstrip()` (kanan).
- **Mencari Awalan/Akhiran**: `.startswith("teks")` dan `.endswith("teks")`.
- **Memisah dan Menggabung**: `.split()` (memecah kalimat jadi List) dan `" ".join(list)` (menggabungkan List jadi kalimat).
- **Mengganti Kata**: `.replace("lama", "baru")`.
- **Format**: `.zfill(5)` (menambah angka 0 di depan, misal: `00042`).
- **Escape Character**: Menggunakan `\n` (baris baru) atau `\t` (tab).
- **Raw String**: Menambahkan huruf `r` sebelum tanda kutip (`r"..."`) agar tanda backslash `\` murni dibaca sebagai teks biasa.

## Hari 4: Operasi List, Set, dan String
- **Panjang/Jumlah Data**: `len(data)` menghitung jumlah item atau huruf.
- **Maks/Min**: `max(data)` dan `min(data)` mencari angka terbesar/terkecil dalam kumpulan data.
- **Menghitung Kemunculan**: `.count(nilai)` menghitung berapa kali suatu nilai/huruf muncul.
- **Pengecekan Anggota**: `in` dan `not in` menghasilkan boolean (`True`/`False`).
- **Multiple Assignment**: `baju, ukuran = ["Kemeja", "L"]`.
- **Mengurutkan Data List**: `.sort()` untuk mengurutkan (A-Z) dan `.sort(reverse=True)` untuk mengurutkan terbalik (Z-A). Tambahkan `key=str.lower` agar pengurutan tidak pilih kasih antara huruf kapital dan kecil.

## Hari 5: Jenis-Jenis Operator
- **Aritmetika**: 
  - `+` (tambah), `-` (kurang), `*` (kali)
  - `/` (pembagian riil, hasil desimal)
  - `//` (pembagian bulat, angka koma dibuang)
  - `%` (modulo / sisa pembagian)
  - `**` (pangkat).
- **Relasional (Perbandingan)**: `==` (sama dengan), `!=` (tidak sama), `>`, `<`, `>=`, `<=`. (Selalu menghasilkan `True`/`False`).
- **Logika**: 
  - `and`: Bernilai True jika *keduanya* True.
  - `or`: Bernilai True jika *salah satu* True.
  - `not`: Membalikkan nilai (contoh `not True` menjadi `False`).
- **Assignment**: `+=`, `-=`, `*=`, `/=`, `%=`. (Jalan pintas untuk mengubah nilai variabelnya sendiri, misal `x += 5` sama artinya dengan `x = x + 5`).

---
*Catatan ini akan terus diupdate seiring berjalannya proses belajar Anda!*
