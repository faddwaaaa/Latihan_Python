# gaji pokok
gaji_pokok = 300000

# input
namakaryawan = input("Nama Karyawan : ")
golongan = int(input("Golongan Jabatan : "))
tingkat_pendidikan = input("Pendidikan : ")
jam_kerja = int(input("Jumlah Jam Kerja : "))

# golongan
if golongan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan == 3:
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0

# tingkat pendidikan
if tingkat_pendidikan == "SMA":
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif tingkat_pendidikan == "D1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif tingkat_pendidikan == "D3":
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif tingkat_pendidikan == "S1":
    tunjangan_pendidikan = 0.30 * gaji_pokok
else:
    tunjangan_pendidikan = 0

# jam kerja
if jam_kerja > 8:
    honor_lembur = (jam_kerja - 8) * 3500
else:
    honor_lembur = 0

# total gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

# format rupiah
def rupiah(angka):
    return f"{angka:,.0f}".replace(",", ".")

# output
print("\n")
print(f"Karyawan yang bernama {namakaryawan}")
print("Honor yang diterima")
print(f"Tunjangan Jabatan       Rp {rupiah(tunjangan_jabatan)}")
print(f"Tunjangan Pendidikan    Rp {rupiah(tunjangan_pendidikan)}")
print(f"Honor Lembur             Rp {rupiah(honor_lembur)}")
print("                       ----------- +")
print(f"Total Gaji              Rp {rupiah(total_gaji)}")
print("(Gaji pokok + tunjangan + lembur)")