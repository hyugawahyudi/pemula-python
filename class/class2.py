# class knp class ini diatas karna python ini interpreted lengguege (harus berurutan)
class mahasiswa():
    nama = 'nama'
# method
    def belajar(self,kondisi):
        print(self.nama,'sedang belajar',kondisi)

    def tidur(self):
        print(self.nama,'tidur dikelas')

# main programmya
otong = mahasiswa()
ucup = mahasiswa()

otong.nama = 'otong surotong'
ucup.nama = 'michael ucup'

otong.belajar('dengan giat')
ucup.tidur()