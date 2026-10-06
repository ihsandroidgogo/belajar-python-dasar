# Tabel Perkalian Nested Loop

print("Tabel Perkalian 1-5:")
for i in range(1,6):
    for j in range(1,6):
        hasil = i * j
        print(f"{i} x {j} = {hasil}")
    print("-----------------")  # Menambahkan baris kosong setelah setiap tabel perkalian

# Contoh Kedua 

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for row in matrix:
    for cell in row:
        print(cell, end=" ")
    print()