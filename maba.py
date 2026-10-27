nis = int(input("Masukkan NIS : "))
nama = input("Masukkan Nama : ")
kodejurusan = input("Masukkan Kode Jurusan : ")

if kodejurusan == "SI" :
    nama_prodi = "Sistem Informasi"
    biaya = 2400000
elif kodejurusan == "SIA" :
    nama_prodi = "Sistem Informasi Akuntansi"
    biaya = 2000000
else :
    print("Jurusan yang anda masukkan salah")

print("------------------------------------")
print("Nis : ", nis)
print("Nama : ", nama)
print("Jurusan : ", nama_prodi)
print("Biaya : ", biaya)
