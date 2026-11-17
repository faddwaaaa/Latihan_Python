def garis():
    print("-------------------------------------------------")

def pilihan():
    if gol[a] == 1 :
        gapok.append(1500000)
        tunj.append(0.02*gapok[a])
        bonus.append(0.01*gapok[a])
    elif gol[a] == 2 :
        gapok.append(1750000)
        tunj.append(0.02*gapok[a])
        bonus.append(0.01*gapok[a])
    elif gol[a] == 3 :
        gapok.append(2000000)
        tunj.append(0.03*gapok[a])
        bonus.append(0.02*gapok[a])
    elif gol[a] == 4 :
        gapok.append(2500000)
        tunj.append(0.03*gapok[a])
        bonus.append(0.02*gapok[a])

    totgaji.append(gapok[a]+tunj[a]+bonus[a])

import os
os.system("cls")

#pengenalan variable
nama = []
gol = []
gapok = []
tunj = []
bonus = []
totgaji = []
j = []

ulang = 1
while j != "n" and j != "N" :
    os.system("cls")
    print("Data Ke -",ulang)
    nama.append(input("Masukkan Nama Karyawan : "))
    gol.append(int(input("Masukkan Golongan [1/2/3/4] : ")))

    j = input("\nTambah data lagi [Y/N] : ")
    ulang += 1

os.system("cls")
print("Daftar Gaji Karyawan")
print("PT. Sejahtera Selamanya")
print("Oktober 2026")
garis()
print("No.  Nama    Golongan Gaji   Tunjangan  Bonus   Total")
print("    Karyawan          Pokok             Gaji")
garis()
no = 1
for a in range(len(nama)):
    # menentukan gaji pokok, tunjungan dan bonus
    pilihan()
    jmlgaji = sum(totgaji)
    print("%i\t%s\t  %i\t  %9d\t%6d\t%6d\t%9d" % (no, nama[a], gol[a], gapok[a], tunj[a], bonus[a], totgaji[a]))
    no = no+1
garis()
print("Total gaji seluruh karyawan :" '{0:,.0f}'.format(jmlgaji))
garis()