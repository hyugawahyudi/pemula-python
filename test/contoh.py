# script input 
kode_baju = input("Masukkan Kode Baju [SP/AD] :")
ukuran = input("Masukkan Ukuran Baju [M/S] :")
# script proses percabangan
if kode_baju == "SP" or kode_baju == "sp" :
    merk = "SuperDry"
    if ukuran == "S" or ukuran == "s" :
        harga = 450000
    elif ukuran == "M" or ukuran == "m" :
        harga : 500000
    else:
        harga = 0
elif kode_baju == "AD" or kode_baju == "ad" :
    merk = "Adidas"
    if ukuran == "S" or ukuran == "s" :
        harga = 650000
    elif ukuran == "M" or ukuran == "m" :
        harga = 700000
    else:
        harga = 0
else:
    merk = "Anda salah masukkan kode baju"
    harga = 0
# script output
print("======================")
print("Merk Baju :",merk)
print("Harga Baju : Rp.",harga)