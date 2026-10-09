# Function sederhana
def sapa_nama(nama):
    print(f"Hello, {nama}!")

# Panggil fungsi
sapa_nama("Ihsan")
sapa_nama("Ayana")

def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")

hitung_luas_persegi_panjang(5, 3)

def hitung_luas_lingkaran(radius):
    pi = 3.14
    luas = pi * radius * radius
    return luas

luas_lingkaran_satu = hitung_luas_lingkaran(7)
luas_lingkaran_dua = hitung_luas_lingkaran(14)

print(f"Luas lingkaran dengan jari-jari 7 adalah {luas_lingkaran_satu}")
print(f"Luas lingkaran dengan jari-jari 14 adalah {luas_lingkaran_dua}")
print(f"Jumlah luas kedua lingkaran adalah {luas_lingkaran_satu + luas_lingkaran_dua}")

# default parameter
def sapa(nama,sapaan="Halo"):
    print(f"{sapaan}, {nama}!")

sapa("Ihsan")
sapa("Ayana", "Selamat Pagi")
sapa("Mona", "Selamat Siang")

#keyword argument
def perkenalan(nama, umur, kota):
    print(f"Nama saya {nama}, umur saya {umur} tahun, dan saya tinggal di {kota}.")

# Panggil fungsi dengan keyword argument
perkenalan(nama="Ihsan", umur=25, kota="Jakarta")
perkenalan(kota="Bandung", nama="Ayana", umur=30)

# local variable
def fungsi_test():
    x = 10  # Local variable
    print(f"Nilai x di dalam fungsi: {x}")  

# print(x) # Akan menghasilkan error karena x tidak dapat diakses di luar fungsi
fungsi_test()

nama_global = "Mona"  # Global variable

def tampil_nama():
    print(f"Nama global di dalam fungsi: {nama_global}")  # Mengakses variabel global

def ubah_nama():
    global nama_global  # Menyatakan bahwa kita ingin mengubah variabel global
    nama_global = "Ihsan"  # Mengubah nilai variabel global
    print(f"Nama global di dalam fungsi setelah diubah: {nama_global}")

tampil_nama()  # Akan menampilkan "Mona"
ubah_nama()    # Akan mengubah nama_global menjadi "Ihsan"
ubah_nama()    # Akan menampilkan "Ihsan"