angka_rahasia = 17

while True:
    tebakan = int(input("Tebak angka rahasia (antara 1 dan 20): "))
    
    if tebakan == angka_rahasia:
        print("Selamat! Tebakanmu benar.")
        break
    elif tebakan < angka_rahasia:
        print("Tebakanmu terlalu rendah. Coba lagi.")
    else:
        print("Tebakanmu terlalu tinggi. Coba lagi.")