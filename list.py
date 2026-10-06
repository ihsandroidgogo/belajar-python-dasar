daftar_kosong = []

angka = [1, 2, 3, 4, 5]
print("Daftar angka:", angka)

nama = ["ihsan","Mona","Ayana"]
print("Daftar nama:", nama)

# List Campuran

campuran = [1, "dua", 3.0, True]
print("Daftar campuran:", campuran)

buah = ["apel", "mangga", "jambu"]
print(buah[1]) # Output: mangga

buah[1] = "pisang"

print(buah)

buah.append("jeruk")

print(buah)

buah.insert(1, "mangga")

print(buah)

buah.remove("mangga")

print(buah)

buah.pop(1)

print(buah)

print(len(buah))

print("mangga" in buah)

# Loop pada List

for item in buah:
    print(item)

# List + if
angka = [10, 15, 20, 25, 30]

for angka_sekarang in angka:
    if angka_sekarang > 20:
        print(angka_sekarang)

# sort() untuk mengurutkan List

angka = [5, 2, 8, 1, 3]

angka.sort()

print(angka)

# Menghitung kemunculan data dengan count()

print(angka.count(2))

'''
Hasil:

3

Artinya angka 2 muncul sebanyak 3 kali.
'''