a = [
    [1,2],
    [3,4]
]

b = [
    [5,6],
    [7,8]
]
hasil = []

for i in range(2):
    baris = []

    for j in range(2):
        jumlah = a[i][j] + b[i][j]
        baris.append(jumlah)

    hasil.append(baris)
print("Hasil Penjumlahan Matriks:")
for baris in hasil:
    print(baris)