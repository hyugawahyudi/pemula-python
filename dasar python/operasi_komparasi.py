# operasi kpmparasi 
# setiap hasil dari komperasi adalah boolean
# >,<,>=,<=,==,!=,is,is not

a = 4 
b = 2

# lebih besar dari >

print("=============== Lebih Beasar dari (>)")
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
hasil = b > 2
print(b,">",2,"=",hasil)

# kurang dari (<)
print("=============== kurang kecil (<)")
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = b < 2
print(b,"<",2,"=",hasil)

# lebih dari atau sama dengan (>=)
print("=============== Lebih Beasar dari (>=)")
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = b >= 3
print(b,">=",3,"=",hasil)
hasil = b >= 2
print(b,">=",2,"=",hasil)

# kurang dari atau sama dengan (<=)
print("=============== kurang kecil (<=)")
hasil = a <= 3
print(a,"<=",3,"=",hasil)
hasil = b <= 3
print(b,"<=",3,"=",hasil)
hasil = b <= 2
print(b,"<=",2,"=",hasil)

# sama dengan (==)
print('================== Sama dengan (==)')
hasil = a == 4
print(a,"==",4,"=",hasil)
hasil = b == 3
print(b,"==",3,"=",hasil)

# sama dengan (!=)
print('================== Sama dengan (!=)')
hasil = a != 4
print(a,"!=",4,"=",hasil)
hasil = b != 3
print(b,"!=",3,"=",hasil)

print('================= object identity (is)')
x = 5 # ini adalah assignment membuat object
y = 5 # 5 ini literal
print('nilai x',x,',id',hex(id(x)))
print('nilai y',y,',id',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

print('================= object identity (is not)')
x = 5 # ini adalah assignment membuat object
y = 6 # 5 ini literal
print('nilai x',x,',id',hex(id(x)))
print('nilai y',y,',id',hex(id(y)))
hasil = x is not y
print('x is not y =',hasil)





# >>> x = 5
# >>> x
# 5   
# >>> type(x)
# <class 'int'>
# >>> id(x)
# 2528845588912
# >>> hex(id(x))
# '0x24ccaf169b0'