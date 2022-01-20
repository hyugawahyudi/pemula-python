# program menghitung badan cm ke m

# cm = int(input("Masukkan Tinggi Badan :"))
# m = cm/100
# print(m)

# if cm >= 176 :
#     print("sangat tinggi")
# elif cm >= 160 :
#     print("tinggi")
# elif cm >= 145 :
#     print("sedang")
# elif cm <= 130 :
#     print("pendek")

# program menentukan yang terkecil

angka = int(input("masukkan angka :"))
angka_1 = int(input("masukkan angka_1 :"))
angka_2 = int(input("masukkan angka_3 :"))

if angka > angka_1 and angka < angka_2 :
    print(angka)
if angka_1 > angka and angka_1 < angka_2 :
    print(angka_1)
if angka_2 > angka_1 and angka_2 < angka :
    print(angka_2)

# Aplikasi menghitung pajak barang
Harga_barang = int(input("Berapa harga barangnya :"))
Pajak = Harga_barang*10/100
print(Pajak)

if Harga_barang >= 1000000 :
    print("Jumlah pajak adalah Rp.",Pajak)
else:
    print("Tidak ada pajak")
    