# operasi dan menipulasi string 

# 1. menyambung string (contenate)
Nama_pertama = "Yoga"
Nama_tengah = "D"
Nama_akhir = "Jancok"

Nama_lengkap = Nama_pertama + " " + Nama_tengah + "'" + Nama_akhir
print(Nama_lengkap)

# 2. menghitung panjang dari string 
panjang = len(Nama_lengkap)
print("panjang dari " + Nama_lengkap + "=" + str(panjang))

# 3. operator untuk string 

# mengecek apakah ada komponen char(karakter) atau string di string 

d = "d"
status = d in Nama_lengkap
print(d + " ada di " + Nama_lengkap + "=" + str(status))

D = "D"
status = d in Nama_lengkap
print(D + " ada di " + Nama_lengkap + "=" + str(status))

d = "d"
status = d not in Nama_lengkap
print(d + " ada di " + Nama_lengkap + "=" + str(status))

# mengulang string 
print("ha"*10)
print(15*"ah")

# indexing 
print("indek ke-0  :" + Nama_lengkap[0]) # dimulai dari 0
print("indek ke-0  :" + Nama_lengkap[6])
print("indek ke-[-1]  :" + Nama_lengkap[-1]) #kalau (-) mengambil dari belakang
print("indek ke-[-2]  :" + Nama_lengkap[-2])
print("indek ke-[0:5]  :" + Nama_lengkap[0:5])
print("indek ke-[7:13]  :" + Nama_lengkap[7:13])
print("indek ke-[0,2,4,6,8,10]  :" + Nama_lengkap[0:10:2])

# item paling kecil
print("paling kecil :" + min(Nama_lengkap))
# item paling besar
print("paling besar :" + max(Nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 39
print("char untuk ASCII 39 adalah " + chr(data))

# 4. operator dalam bentuk method 

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))