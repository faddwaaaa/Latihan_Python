matriks = []
for i in range(2):
    baris = []

    for j in range(3):
        angka = int(input(f"Masukkan angka baris {i+1} kolom {j+1} :"))
        baris.append(angka)

    matriks.append(baris)

print("\nHasil Matriks:")
for baris in matriks:
    print(baris)