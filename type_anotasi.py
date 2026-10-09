# Variable dengan type

nama: str = "Ihsan"
umur: int = 31
tinggi: float = 1.75
lulus: bool = True
print(f"Halo nama saya {nama} dan umur {umur}")

# Fungsi
def tambah(a: int, b: int) -> int:
    hasil = a + b
    return hasil

print(f"Hasil Pertambahan adalah {tambah(5, 2)}")