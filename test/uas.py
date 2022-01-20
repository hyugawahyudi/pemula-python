print("\n ============ UAS =========")
# nomer 1
data = ["Teknologi Informasi","Informatika","Sistem Informasi","Rekayasa Perangkat Lunak","Teknik Elektro"]
# nomer 2
for i in data :
    print(i)

print("="*20)
# nomer 3
jurusan = {
    "TI" : "Teknologi Informasi",
    "IF" : "Informatika",
    "SI" : "Sistem Informasi",
    "RPL": "Rekayasa Perangkat Lunak",
    "TE" : "Teknik Elektro",
}
# nomer 4
for k in jurusan :
    print(k,":" ,jurusan[k])

print("="*20)
# nomer 5
def rata2 (input1,input2,input3):
    hasil = (input1 + input2 + input3)/3
    return hasil
hasil = rata2 (1,2,3)
print(hasil)

print("="*20)
# nomer 6
nilai = int(input("masukkan input : "))
for j in range(2,nilai,2):
    print(j)

print("="*20)
# nomer 7
total = 0
jumlah = 0
stop = False

while stop == False:
    angka = input('masukkan angka :')

    if angka =="":
        stop = True
    else:
        angka = float (angka)
        jumlah += 1
hasil = jumlah
print("jumlah",hasil)
