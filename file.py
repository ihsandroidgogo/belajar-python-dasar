# print("=== SIMPAN DATA NILAI ===")

# file = open("nilai_siswa.txt", "w")

# while True:
#     nama = input("Nama Siswa (enter untuk selesai): ")
#     if nama == "":
#         break
#     nilai = input("Nilai: ")

#     # tulis ke file
#     file.write(nama + "," + nilai + "\n")
#     print("Data", nama, "berhasil disimpan")

# file.close()
# print("Semua data berhasil disimpan ke nilai_siswa.txt")

# print("=== MENAMPILKAN DATA NILAI ===")
# file = open("nilai_siswa.txt","r")

# for line in file:
#     data = line.strip().split(",")
#     print(data[0], ":", data[1])

# file.close()
# print("=== SELESAI ===")

# Menampilkan data (REKOMENDASI)
print("=== MENAMPILKAN DATA NILAI ===")

try:
    with open("nilai_siswa.txt","r") as file:
        for line in file:
            data = line.strip().split(",")
            print(data[0], ":", data[1])
except FileNotFoundError:
    print("File tidak ditemukan")

print("=== SELESAI ===")

# Bisa nanti di Comment/Uncomment ketika di pakai