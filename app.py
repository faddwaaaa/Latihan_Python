kode_baju = input("Masukkan Kode Baju [SP/AD] : ")
ukuran = input("Masukkan Ukuran Baju [S/M] : ")

if kode_baju == "SP" or kode_baju == "sp":
    merk = "SuperDry"
    if ukuran == "S" or ukuran == "s":
        harga = 450000
    elif ukuran == "M" or ukuran == "m":
        harga = 500000
    else:
        harga = 0

elif kode_baju == "AD" or kode_baju == "ad":
    merk = "Adidas"
    if ukuran == "S" or ukuran == "s":
        harga = 650000
    elif ukuran == "M" or ukuran == "m":
        harga = 700000
    else:
        harga = 0

else:
    merk = "Kode Baju Salah"
    harga = 0

print("------------------------")
print("Merk Baju :", merk)
print("Harga Baju : Rp.", harga)