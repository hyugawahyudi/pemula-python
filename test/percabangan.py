# konversi nilai angka menjadi nilai huruf

input = int(input("masukkan nilai angka :"))

if input >= 80 :
    print("A")
elif input >= 70 :
    print("B")
elif input >= 50 :
    print("C")
elif input >= 30 :
    print("D")
else:
    print("E")

# aplikasi untuk menghitung umur

tahun_lahir = int(input("masukkan tahun lahir anda :"))

# umur = tahun sekarang - tahun lahir 
umur = 2021 - tahun_lahir
print("umur anda adalah :",umur)

if umur <= 13 :
    print("anak-anak")
elif umur <= 20 :
    print("remaja")
elif umur <= 39 :
    print("dewasa")
else:
    print("tua")