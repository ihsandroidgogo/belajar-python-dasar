# Contoh Pertama

print("= Kalkulator Sederhana =")

try:
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 / angka2
    print(f"Hasil: {hasil}")
except:
    print("Terjadi kesalahan di input pengguna")

print("= Program Selesai =")

print(" ")

# Contoh Kedua
try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Bukan angka!")
else:
    print(f"Anda memasukkan {angka}")   # jalan jika TIDAK ada error
finally:
    print("Selesai.")                    # SELALU jalan

print(" ")

# Contoh Ketiga
try:
    int(input("Masukkan Angka: "))
except ValueError as e:
    print(f"Terjadi error: {e}")
# Terjadi error: jika yang dimasukan bukan angka dan menangkap pesan error nya.