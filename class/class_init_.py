# class 
class mahasiswa():

    def __init__(self,input_nama,input_nim):
        self.nama = input_nama
        self.nim = input_nim
    

    def belajar(self,kondisi):
        print(self.nama,'sedang belajar',kondisi)

    def tidur(self):
        print(self.nama,'tidur dikelas')

# main programmya
otong = mahasiswa('otong surotong',2021500026)

print(otong.nama)
otong.nama = 'atang suratang'
print(otong.nama)

# print(otong.nim)
# otong.belajar('dengan giat')




