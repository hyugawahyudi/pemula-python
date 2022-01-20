print("====> APLIKASI MENENTUKAN GENAP/GANJIL")
print()

bil = int(input("masukkan bilangan :"))

if bil % 2 == 0 :
    print("%d bilangan genap" % bil)
else :
    print("%d bilangan ganjil" % bil)

print ("=====> APLIKASI JUAL BELI SEDERHANA")
print()

total_beli = int(input("masukkan total beli :"))
total_bayar = int(input("masukkan total bayar :"))
kembalian = total_bayar - total_beli
if total_bayar < total_beli :
    print("uang anda kurang")
else :
    print("kembalian anda :",kembalian)

# test 
nilai = int(input("masukkan nilai :"))
if nilai >= 60 :
    print("lulus")
else:
    print("tidak lulus")

# program menentukan negatif/positif
angka = int(input("Masukkan angka :"))
if angka < 0 :
    ket = "bilangan negatif"
else:
    ket = "bilangan positif"
print("angka",angka,ket)
