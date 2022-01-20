Barang = ['kucing','ember','jaket','ban','mobil']
print(Barang)

# beberapa method yang bisa digunakan untuk menipulasi list 
# method untuk mengubah data ke list 
Barang.append('sepeda')
print(Barang)

Barang.extend('dompet')
print(Barang)

Barang.insert(3,'sepeda')
print(Barang)

# method untuk menghitung anggota
jumlaSepeda = Barang.count('sepeda')
print('jumlah sepeda adalah ',jumlaSepeda)

Barang.remove('sepeda') #mengremove data yg ketemu pertama kali
print(Barang)

Barang.reverse()
print(Barang)

print('='*35)
Data = Barang.copy()
Data.append('gelas')
print(Data)
print(Barang)