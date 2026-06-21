# ==========================================
# CONTOH MATERI: TIPE DATA PYTHON
# ==========================================

print("--- 1. TIPE DATA PRIMITIF ---")

# a. Integer (Bilangan Bulat)
umur = 25
print("Integer:", umur, "| Tipe:", type(umur))

# b. Float (Bilangan Desimal)
berat_badan = 65.5
print("Float:", berat_badan, "| Tipe:", type(berat_badan))

# c. Complex (Bilangan Kompleks)
bil_kompleks = 1 + 2j
print("Complex:", bil_kompleks, "| Tipe:", type(bil_kompleks))

# d. Boolean (Benar/Salah)
is_student = True
print("Boolean:", is_student, "| Tipe:", type(is_student))

# e. String (Teks)
nama = "Daviano"
print("String:", nama, "| Tipe:", type(nama))

# Metode String: Indexing dan Slicing
teks = "Dicoding"
print("Huruf pertama (Index 0):", teks[0])
print("Slicing (Index 2 ke akhir):", teks[2:])
print(f"Formatted String: Halo, nama saya {nama} dan umur saya {umur} tahun.\n")


print("--- 2. TIPE DATA COLLECTION ---")

# a. List (Berurutan, bisa diubah/Mutable)
buah_list = ["Apel", "Mangga", "Jeruk"]
buah_list[0] = "Pisang" # Mengubah isi list
print("List:", buah_list, "| Tipe:", type(buah_list))

# b. Tuple (Berurutan, TIDAK bisa diubah/Immutable)
warna_tuple = ("Merah", "Kuning", "Hijau")
# warna_tuple[0] = "Biru" # <- Jika tanda '#' dihapus, baris ini akan menyebabkan error
print("Tuple:", warna_tuple, "| Tipe:", type(warna_tuple))

# c. Set (Tidak berurutan, unik)
angka_set = {1, 2, 2, 3, 3, 4} # Angka duplikat (2 & 3) akan otomatis diabaikan
print("Set (Unik):", angka_set, "| Tipe:", type(angka_set))

# d. Dictionary (Pasangan Key-Value)
profil_dict = {
    "nama": "Daviano",
    "pekerjaan": "Developer",
    "umur": 20
}
profil_dict["pekerjaan"] = "Data Scientist" # Mengubah value berdasarkan key
print("Dictionary:", profil_dict)
print("Akses value dengan key 'nama':", profil_dict["nama"])
print()


print("--- 3. KONVERSI TIPE DATA ---")

# Dari String ke Integer
angka_string = "100"
angka_integer = int(angka_string)
print("Dari String ke Integer:", angka_integer, type(angka_integer))

# Dari Float ke Integer (Desimalnya dipotong)
desimal = 9.99
bulat = int(desimal)
print("Dari Float ke Integer:", bulat, type(bulat))

# Konversi string menjadi list
huruf_list = list("Halo")
print("String diubah ke List:", huruf_list)
