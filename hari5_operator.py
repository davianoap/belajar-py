# ==========================================
# CONTOH MATERI: JENIS-JENIS OPERATOR
# ==========================================

print("--- 1. OPERATOR ARITMETIKA ---")
x = 11
y = 5
print(f"x = {x}, y = {y}")
print("Penjumlahan (x + y)    :", x + y)
print("Pengurangan (x - y)    :", x - y)
print("Perkalian   (x * y)    :", x * y)
print("Pembagian Riil (x / y) :", x / y)      # Menghasilkan angka desimal
print("Pembagian Bulat(x // y):", x // y)     # Menghasilkan angka bulat (pecahan dibuang)
print("Modulo/Sisa (x % y)    :", x % y)      # Sisa pembagian (11 dibagi 5 sisanya 1)
print("Pangkat     (x ** y)   :", x ** y)     # 11 pangkat 5
print()

print("--- 2. OPERATOR RELASIONAL (PERBANDINGAN) ---")
# Hasil dari operator relasional selalu Boolean (True/False)
a = 5
b = 10
print(f"a = {a}, b = {b}")
print("a == b (Sama dengan)        :", a == b)
print("a != b (Tidak sama dengan)  :", a != b)
print("a > b  (Lebih besar dari)   :", a > b)
print("a < b  (Lebih kecil dari)   :", a < b)
print("a >= b (Lebih besar/sama)   :", a >= b)
print("a <= b (Lebih kecil/sama)   :", a <= b)
print()

# Perbandingan pada String (Berdasarkan urutan Abjad/tabel ASCII)
kata1 = "Dicoding"
kata2 = "Indonesia"
print(f"Bandingkan string: '{kata1}' dengan '{kata2}'")
print(f"{kata1} == {kata2} :", kata1 == kata2)
print(f"{kata1} < {kata2}  :", kata1 < kata2) # 'D' muncul lebih dulu dari 'I' di tabel alfabet/ASCII, jadi 'D' dianggap lebih kecil
print()

print("--- 3. OPERATOR LOGIKA ---")
# Logika AND (Hanya True jika KEDUANYA True)
print("True and True   :", True and True)
print("True and False  :", True and False)

# Logika OR (Akan True jika SALAH SATU atau KEDUANYA True)
print("True or False   :", True or False)
print("False or False  :", False or False)

# Logika NOT (Membalikkan nilai / Negasi)
print("not True        :", not True)
print("not False       :", not False)
print()

print("--- 4. OPERATOR ASSIGNMENT ---")
# Menyingkat penulisan untuk memberikan nilai ke sebuah variabel
angka = 10
print("Nilai awal 'angka' :", angka)

angka += 5  # Sama dengan: angka = angka + 5
print("Setelah angka += 5 :", angka)

angka -= 3  # Sama dengan: angka = angka - 3
print("Setelah angka -= 3 :", angka)

angka *= 2  # Sama dengan: angka = angka * 2
print("Setelah angka *= 2 :", angka)

angka /= 4  # Sama dengan: angka = angka / 4
print("Setelah angka /= 4 :", angka)
