print("====== TOKO BUKU MAHASISWA ======")
nama = input("Masukkan nama anda: ")
judulbuku = input("Masukkan judul buku yang dibeli: ")
hargabuku = int(input("Masukkan harga buku (Rp): "))
jumlahbuku = int(input("Masukkan jumlah buku yang dibeli: "))

print("\n====== STRUK BELANJA ======")
print(f"Nama Pembeli : {nama}")
print(f"Buku Dibeli : {judulbuku}")
print(f"Harga Satuan : Rp {hargabuku:,}")
print(f"Jumlah Beli : {jumlahbuku} pcs")
print("------------------------------------")
totalbayar = hargabuku * jumlahbuku
print(f"Total Bayar : Rp {totalbayar:,}")
print("====================================")

uangbayar = int(input("\nMasukkan uang bayar : "))
uangkembali = uangbayar - totalbayar
print(f"Uang Kembali : Rp {uangkembali:,}")
print("Terima kasih telah berbelanja di Toko Buku Mahasiswa")