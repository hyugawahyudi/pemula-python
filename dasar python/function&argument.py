# fungsi dengan menggunakan argument sederhana
# def siswa(nama):
#     print('siswa ini bernama :',nama)

# siswa('yoga')

# fungsi dengan menggunakan keywords argument

# def guru(nama,pelajaran):
#     print('guru ini bernama :',nama)
#     print('mengajar :',pelajaran)

# guru(nama='tut',pelajaran='mtk')
# guru(pelajaran='algodata',nama='set')
# guru('olahraga','jay') #ini contoh yang salah

# fungsi dengan menggunakan defult argument 
def penjagaSekolah(nama,shift='siang',galak='tidak'):
    print('penjaga sekolah ini bernamam:',nama)
    print('shiftnya:',shift)
    print('galak ?',galak)

penjagaSekolah('kentis')
penjagaSekolah('mamang',shift='malam')
penjagaSekolah('abay',galak='sangat')
penjagaSekolah(shift='malam',galak='sangat')# menghasilkan eror