# ==========================================
# CONTOH MATERI: TRANSFORMASI STRING (HARI 3)
# ==========================================

print("--- 1. MENGUBAH HURUF BESAR/KECIL ---")
teks = "Halo Python"
print("Asli   :", teks)
print("Upper  :", teks.upper())
print("Lower  :", teks.lower())
print()

print("--- 2. MENGHAPUS SPASI / KARAKTER ---")
spasi_teks = "   Dicoding   "
print("Asli (pakai spasi) :", repr(spasi_teks))
print("Strip (kiri & kanan):", repr(spasi_teks.strip()))
print("Lstrip (kiri)      :", repr(spasi_teks.lstrip()))
print("Rstrip (kanan)     :", repr(spasi_teks.rstrip()))

print("\n--- 3. CEK AWALAN & AKHIRAN ---")
kata = "Dicoding Indonesia"
print(f"Kalimat: '{kata}'")
print("Cek startswith('Dicoding'):", kata.startswith("Dicoding"))
print("Cek endswith('Python')    :", kata.endswith("Python"))
print()

print("--- 4. MEMISAH DAN MENGGABUNG STRING ---")
# Split (Memisah string menjadi List)
kalimat = "Belajar Python itu seru"
kata_list = kalimat.split() # Dipisah berdasarkan spasi (default)
print("Hasil split():", kata_list)

# Join (Menggabungkan List menjadi String)
gabungan = " - ".join(["Satu", "Dua", "Tiga"])
print("Hasil join():", gabungan)
print()

print("--- 5. MENGGANTI ELEMEN (REPLACE) ---")
teks_lama = "Ayo belajar Java"
teks_baru = teks_lama.replace("Java", "Python")
print("Teks Asli :", teks_lama)
print("Teks Baru :", teks_baru)
print()

print("--- 6. PENGECEKAN KONDISI STRING ---")
print("Apakah 'PYTHON' isupper? :", "PYTHON".isupper())
print("Apakah 'python' islower? :", "python".islower())
print("Apakah 'Python123' isalpha? (Hanya huruf):", "Python123".isalpha())
print("Apakah 'Python123' isalnum? (Huruf/Angka):", "Python123".isalnum())
print("Apakah '123' isdecimal? (Hanya Angka)    :", "123".isdecimal())
print("Apakah '    ' isspace? (Hanya Spasi)     :", "    ".isspace())
print("Apakah 'Halo Dunia' istitle? (Kapital Awal):", "Halo Dunia".istitle())
print()

print("--- 7. FORMATTING STRING (RATA KIRI/KANAN & ZFILL) ---")
print("zfill(5)    :", "42".zfill(5))  # Menambah angka 0 di depan
print("rjust(10, '*'):", "Python".rjust(10, '*')) # Rata Kanan (ditambah *)
print("ljust(10, '-'):", "Python".ljust(10, '-')) # Rata Kiri (ditambah -)
print("center(12, '='):", "Python".center(12, '=')) # Rata Tengah
print()

print("--- 8. ESCAPE CHARACTER & RAW STRING ---")
# Escape Character (\', \n, \t)
teks_escape = "Hari Jum\'at\nKita belajar\tPython"
print("Contoh Escape Character:")
print(teks_escape)
print()

# Raw String (r"...") sangat berguna agar backslash (\) tidak dianggap perintah
teks_raw = r"Folder\baru\test.txt"
print("Contoh Raw String:")
print(teks_raw)
