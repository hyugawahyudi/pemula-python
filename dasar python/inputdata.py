# mengambil input data dari user

# data yang dimasukkan pasti string
data = input("masukkan data :")
print("data :",data,",type :",type (data))

# jika kita mengambil integer/float
angka = int(input("masukkan angka:"))
angka = float(input("masukkan angka:"))
print("data :",angka,",type :",type(angka))

# bagaimana dengan boolean
biner = bool(int(input("masukkan nilai boolean :")))
print("data :",biner,",type",type(biner))