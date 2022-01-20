# operator logika atau boolean
# digunakan untuk membandingkan 2 kondisi logika

""" operator  keterangan                                                contoh
    1. and    bernilai benar jika semua kondisi benar                   x < 5 and x < 10 
    2. or     bernilai benar jika salah satu kondisi benar              x < 5 or x < 4
    3. not    membalik hasil,jika benar maka salah atau sebaliknya not (x < 5 and x < 10) """

# tabel logika

""" x           y           x and y     x or y      not x       not(x and y)
    true        true        true        true        false       false
    true        false       false       true        false       true 
    false       true        false       true        true        true
    false       false       false       false       true        true"""

x = 5
y = 2

print(x == 5 and x < 10)

# not,or,and,xor 

# NOT 
print('==== NOT ====')
a = False 
c = not a
print ('data a =',a)
print('--------- NOT')
print('data c =',c)

# OR (jika salah satu true ,maka hasilnya adalah true)
print('==== OR ====')
a = False 
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False 
b = True
c = a or b
print(a,'OR',b,'=',c)
a = True 
b = False
c = a or b
print(a,'OR',b,'=',c)
a = True 
b = True
c = a or b
print(a,'OR',b,'=',c)

# AND (jika dua buah nilai true ,maka hasilnya adalah true)
print('==== AND ====')
a = False 
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False 
b = True
c = a and b
print(a,'AND',b,'=',c)
a = True 
b = False
c = a and b
print(a,'AND',b,'=',c)
a = True 
b = True
c = a and b
print(a,'AND',b,'=',c)

# XOR (akan true jika salah satu true,sisanya false)
print('==== XOR ====')
a = False 
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False 
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True 
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = True 
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
