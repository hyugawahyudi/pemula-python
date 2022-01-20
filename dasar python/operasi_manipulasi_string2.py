# operator dalam bentuk methods

## merubah case dari string 

# merubah semua ke upper case (merubah kehuruf kapital)

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case (merubah kehuruf kecil)
alay = "aKu KeCe AbieeezZzZZZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "ses"
apakah_lower = salam.islower() # hasil bool
print(salam + " is lower = " + str(apakah_lower))
# contoh pengecekan upper case
salam = "ses"
apakah_upper = salam.isupper() # hasil bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf

data = "kamugila"
apakah_alpha = data.isalpha() 
print(data + " is alpha = " + str(apakah_alpha))

# isalnum() <-- huruf dan angka

data = "yoga112"
apakah_alnum = data.isalnum() 
print(data + " is alnum = " + str(apakah_alnum))

# isdecimal() <-- angka saja

data = "123"
apakah_decimal = data.isdecimal() 
print(data + " is decimal = " + str(apakah_decimal))

# isspace() <-- spasi,tab,newline \n 

data = "\n"
apakah_space = data.isspace() 
print(data + " is space = " + str(apakah_space))

# istitle() <-- semua kata dimulai dengan huruf besar 

judul = "It Is Okay To Be Orkay"
cek_judul = judul.istitle() # hasil bool
print(judul + "is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() <-- keren
cek_start = "Yoga Wahyudi".startswith("Yoga")
print("start = " + str(cek_start))

cek_end = "Yoga Wahyudi".endswith("Wahyudi")
print("end = " + str(cek_end))

# penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' cuk '.join(pisah)
print(gabungan)

gabungan = "akucuksayangcukkamu"
print(gabungan.split('cuk'))

## alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'" +kanan+ "'")

kiri = "kiri".ljust(10)
print("'" +kiri+ "'")

tengah = "tengah".center(20,":")
print("'" +tengah+ "'")

# kebalikannya -> strip()
tengah = tengah.strip(":") # menghilangkan tanda :
print("'" +tengah+ "'")

