# class 
class mahasiswa():

    jumlah_mahasiswa = 0

    def __init__(self,input_nama,input_nim):
        self.nama = input_nama # public
        self.nim = input_nim # public

        mahasiswa.jumlah_mahasiswa += 1

# main programmya (intenses)
otong = mahasiswa('otong surotong',2021500026)
ucup = mahasiswa('michael ucup',2021500022)
cassandra = mahasiswa('cassandra aja',30408520850)

print(mahasiswa.jumlah_mahasiswa)
