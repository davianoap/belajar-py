"""
LATIHAN SOAL HARI 1 - 3
Materi: Variabel, Input/Output, Tipe Data, dan Transformasi String.
Silakan kerjakan di bagian yang bertanda TODO!
"""

print("--- SOAL 1: Variabel dan Input ---")
# TODO: 
# 1. Minta pengguna memasukkan nama mereka dan simpan di variabel `nama`.
# 2. Minta pengguna memasukkan tahun lahir mereka dan simpan di variabel `tahun_lahir_str`.
#    (Gunakan nilai buatan saja untuk saat ini jika tidak ingin pakai input manual, 
#    misal: nama = "Daviano", tahun_lahir_str = "2006")

nama = input("Masukkan nama:   ")            # Silakan ganti dengan input("Masukkan nama: ") jika mau
tahun_lahir_str = input("Masukkan tahun lahir: ")   # Silakan ganti dengan input("Masukkan tahun lahir: ") jika mau

print(f"Halo {nama}, selamat datang di latihan Python!")
print(f"kamu lahir di {tahun_lahir_str}")


print("--- SOAL 2: Tipe Data dan Konversi ---")
# TODO:
# 1. Ubah `tahun_lahir_str` yang asalnya String menjadi Integer. Simpan di `tahun_lahir_int`.
# 2. Hitung umur pengguna di tahun 2026 (2026 - tahun lahir). Simpan di variabel `umur`.
# 3. Buat sebuah Dictionary bernama `profil` yang berisi:
#    - key "nama_lengkap" dengan value dari variabel `nama`
#    - key "umur_sekarang" dengan value dari variabel `umur`
#    - key "status_pelajar" dengan value True (Boolean)

tahun_lahir_int = 0   # Ganti angka 0 dengan kode konversi
umur = 0              # Ganti angka 0 dengan rumus perhitungan umur
profil = {}           # Ganti {} dengan Dictionary yang diminta

print("Profil Anda:", profil)
print()


print("--- SOAL 3: Transformasi String ---")
teks_kotor = "   BeLajaR PyTHon itu mENyeNangKAn   "

# TODO:
# 1. Hapus spasi di awal dan akhir teks_kotor, lalu ubah SEMUA hurufnya menjadi huruf KECIL.
#    Simpan di variabel `teks_bersih`.
# 2. Pisahkan `teks_bersih` menjadi sebuah List (berdasarkan spasi antar kata). 
#    Simpan di variabel `list_kata`.
# 3. Gabungkan kembali kata-kata di dalam `list_kata` menggunakan pembatas " - ".
#    Simpan di variabel `teks_gabung`.

teks_bersih = ""      # Ganti string kosong ini dengan operasi string
list_kata = []        # Ganti list kosong ini dengan operasi pemisahan string
teks_gabung = ""      # Ganti string kosong ini dengan operasi penggabungan string

print("1. Teks Bersih :", repr(teks_bersih))
print("2. List Kata   :", list_kata)
print("3. Teks Gabung :", teks_gabung)
