nim = []
uts = []
uas = []
total = []

ulang = 2 
for i in range(ulang):
    print("data ke-", i+1)
    nim.append(input("Masukkan NIM: "))
    uts.append(int(input("Masukkan Nilai UTS: ")))
    uas.append(int(input("Masukkan Nilai UAS: ")))
for i in range(ulang):
    total.append(uas[i] + uts[i] / 2)

# cetak
print("===============================")
print("NIM   Nilai UTS   Nilai UAS   Total")
for i in range(ulang):
    print ("%s   %i\t  %i\t   %i" % (nim[i],uts[i],uas[i],total[i]))
print("===============================")