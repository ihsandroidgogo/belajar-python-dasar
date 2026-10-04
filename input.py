nama = input("Masukkan nama anda: ")
print(f"Halo, {nama}! Selamat datang di program ini.")

umur = input("Masukkan umur anda: ")
umur = int(umur)  # Mengubah input umur menjadi tipe data integer
print(f"Umur anda adalah {umur} tahun.")
print("Tipe Data", type(nama), "dan", type(umur))