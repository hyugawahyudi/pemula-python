'''perulangan adalah inturksi yang dapat mengulang sederetan intruksi
secara berulang ulang sesuaipersyaratan yang ditetapkan.'''

# perulangan menggunakan while
i = 1 
while i < 5 :
    print(i)
    i += 1


# # statement break dan continue
# """ break = digunakan untuk menhintikan perulangan walau kondisi 
# masih bernilai benar. """


i = 1 
while i < 5 :
    print(i)
    if i == 2:
        break
    i += 1

'''continue = melewati/skip 1 perulangan yang sedang terjadi dan lanjut
keperulangan selanjutnya'''

i = 0
while i < 5 :
    i += 1

    if i == 2:
        continue
    print(i)

# statemen else = digunakan untuk menjalankan blok statemen saat perulangan selesai

i = 0
while i < 5 :
    i += 1

    if i == 2:
        continue
    print(i)
else :
    print('selesai')
