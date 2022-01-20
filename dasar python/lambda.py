def jumlah(a,b):
    c = a*b
    return c

hasil = jumlah(4,5)
# print(hasil)

# membuat anonymous function lambda 
# kali = lambda argumen: print(argumen)
# kali('test')

kali = lambda x,y: x*y
# print(kali(3,4))
hasil = kali(3,4)
print(hasil)