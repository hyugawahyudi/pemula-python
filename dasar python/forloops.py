# list sebagai iterable 
from typing import Iterable

Gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']
for i in Gorengan :
    print(i)
    print(len(i))

# string sebagai Iterable
bakwan = 'bakwan'
for g in bakwan:
    print(g)

# for di dalam for 
Gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']
Buah = ['semangka','jeruk','apel','anggur']
Sayur = ['kangkung','wortel','tomat','kentang']

Daftar_belanja = [Gorengan,Buah,Sayur]
print(Daftar_belanja)

print('='*20)
for subDaftarBelanja in Daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)






