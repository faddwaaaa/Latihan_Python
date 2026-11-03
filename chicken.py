print("GEROBAK FRIED CHICKEN")
print("-----------------------")
print("Kode JenisPotong Harga")
print("-----------------------")
print("D    Dada    Rp. 2500")
print("P    Paha    Rp. 2000")
print("S    Sayap    Rp. 1500")
print("-----------------------")

banyak_jenis = int(input("Banyak Jenis : "))

jenis = []
harga = []
banyak = []
jumlah = []

for i in range(banyak_jenis):
    print("Jenis Ke-", i+1)
    kode = input("Kode Potong [D/P/S] : ")
    beli = int(input("Banyak Potong : "))

    if kode == "D" or kode == "d":
        nama = "Dada"
        harga_satuan = 2500
    elif kode == "P" or kode == "p":
        nama = "Paha"
        harga_satuan = 2000
    elif kode == "S" or kode == "s":
        nama = "Sayap"
        harga_satuan = 1500
    else:
        print("Tidak Ada")
        harga_satuan = 0
    total = harga_satuan * beli

    jenis.append(nama)
    harga.append(harga_satuan)
    banyak.append(beli)
    jumlah.append(total)


print("\nGEROBAK FRIED CHICKEN")
print("---------------------------------------------------------------")
print("No. Jenis Potong Harga Satuan Banyak Beli Jumlah Harga")
print("---------------------------------------------------------------")

for i in range(banyak_jenis):
    print(f"\t{i+1} {jenis[i]} {harga[i]} {banyak[i]} Rp. {jumlah[i]}")

print("---------------------------------------------------------------")
jumlah_bayar = sum(jumlah)
pajak = jumlah_bayar * 10 / 100
total_bayar = jumlah_bayar + pajak

print("Jumlah Bayar: Rp.", jumlah_bayar)
print("Pajak 10%: Rp.", pajak)
print("Total Bayar: Rp.", total_bayar)

