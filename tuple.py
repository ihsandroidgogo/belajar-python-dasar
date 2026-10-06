buah = ("apel", "mangga", "jeruk")

print(buah)

print(buah[0])
print(buah[1])
print(buah[2])

'''
Tuple memang dirancang supaya data di dalamnya tidak dapat diubah secara langsung.
Ini berguna ketika kita memiliki data yang seharusnya tetap.

Tetapi Tuple bisa berisi List
Tuple-nya tidak bisa diganti
Tetapi List di dalamnya masih bisa diubah
'''

print(len(buah))

for item in buah:
    print(item)

# Tuple Unpacking

data = ("Ihsan", 25, "Indonesia")

nama, umur, negara = data

print(nama)
print(umur)
print(negara)

# Mengakses data Tuple dengan index()
print(data.index(25))
