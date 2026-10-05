# Contoh 1

angka = 1
while angka <= 5:
    print(angka)
    angka += 1

# Contoh 2
password = ""

while password != "rahasia":
    password = input("Masukkan password: ")
    if password != "rahasia":
        print("Password salah, coba lagi.")

print("Password benar, akses diberikan.")