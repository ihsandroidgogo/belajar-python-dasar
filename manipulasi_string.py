teks = "Mona Nabilah"

print(teks.upper())


kalimat = "saya suka belajar python"
kata = kalimat.split() # ['saya', 'suka', 'belajar', 'python']
print(kata)

gabung = "-".join(kata)
print(gabung)   # saya-suka-belajar-python

teks_baru = "Saya suka Java"
baru = teks_baru.replace("Java", "Python")
print(baru)  # Saya suka Python

# Slicing
teks_slicing = "Python Programming" # Format slicing adalah: teks[start:stop]
print(teks_slicing[0])      # Karakter pertama
print(teks_slicing[0:6])    # Python
print(teks_slicing[-11:])   # Programming
print(teks_slicing[::-1])   # gnimmargorP nohtyP (reverse string)
print(teks_slicing[::2])    # Pto rgamn (skip 2 karakter)
print(teks_slicing[-1])     # Karakter terakhir