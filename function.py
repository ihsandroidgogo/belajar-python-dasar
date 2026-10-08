def sapa_nama(nama):
    print(f"Hello, {nama}!")

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

def sapa(nama,sapaan="Halo"):
    print(f"{sapaan}, {nama}!")

sapa("Ihsan")
sapa("Ayana", "Selamat Pagi")
sapa("Mona", "Selamat Siang")