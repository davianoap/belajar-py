# ==========================================
# CONTOH MATERI: OPERASI LIST, SET, STRING
# ==========================================

print("--- 1. FUNGSI LEN() ---")
# Menghitung panjang/jumlah elemen data
contoh_list = [1, 3, 5, 7, 9]
contoh_set = {1, 2, 3, 4, 5}
contoh_string = "Belajar Python"

print("Panjang List  :", len(contoh_list))
print("Panjang Set   :", len(contoh_set))
print("Panjang String:", len(contoh_string)) # Spasi dihitung sebagai 1 karakter
print()

print("--- 2. FUNGSI MIN() & MAX() ---")
# Mencari nilai terkecil (minimum) dan terbesar (maksimum)
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print("List Angka    :", angka)
print("Nilai Minimum :", min(angka))
print("Nilai Maksimum:", max(angka))
print()

print("--- 3. FUNGSI COUNT() ---")
# Menghitung berapa kali suatu data muncul
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print("List Genap                :", genap)
print("Jumlah angka 6 pada list  :", genap.count(6))

teks = "Belajar Python di Dicoding sangat menyenangkan"
print("Kalimat                   :", teks)
print("Jumlah huruf 'a' pada teks:", teks.count("a"))
print()

print("--- 4. OPERATOR 'IN' & 'NOT IN' ---")
# Mengecek apakah nilai tertentu ada di dalam suatu data (mengembalikan True/False)
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print("Apakah 'Dicoding' ada?      :", 'Dicoding' in kalimat)
print("Apakah 'tidak' ada?         :", 'tidak' in kalimat)
print("Apakah 'Dicoding' TIDAK ada?:", 'Dicoding' not in kalimat)
print()

print("--- 5. MULTIPLE VARIABLE ASSIGNMENT ---")
# Memberikan nilai ke banyak variabel sekaligus dari isi List/Tuple
data = ['Kemeja', 'Putih', 'L']
apparel, color, size = data # Jumlah variabel di kiri harus sama dengan isi list di kanan

print("Data asli:", data)
print("Apparel  :", apparel)
print("Color    :", color)
print("Size     :", size)
print()

print("--- 6. FUNGSI SORT() ---")
# Mengurutkan data pada List
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort() # Mengurutkan sesuai Abjad (Ascending A-Z)
print("Sort Biasa (A-Z)    :", kendaraan)

kendaraan.sort(reverse=True) # Mengurutkan terbalik (Descending Z-A)
print("Sort Terbalik (Z-A) :", kendaraan)

# Mengurutkan dengan mengabaikan huruf kapital menggunakan parameter 'key=str.lower'
campur = ['motor', 'mobil', 'Helikopter', 'Pesawat']
campur.sort(key=str.lower)
print("Sort (abaikan kapital):", campur)
