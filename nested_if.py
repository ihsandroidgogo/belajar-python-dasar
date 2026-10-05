# Contoh Pertama
saldo = 500_000
pin_benar = True

if pin_benar:
    if saldo >= 100_000:
        print("Penarikan berhasil")
    else:
        print("Saldo tidak cukup")
else:
    print("PIN salah")



# Contoh Kedua

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == "admin" and password == "admin123":
        print("Login berhasil")
        print("Selamat datang, admin!")
else:
    print("Username atau password salah")


# Jangan terlalu dalam. Kalau sudah lebih dari 2 tingkat, biasanya bisa disederhanakan dengan "and".