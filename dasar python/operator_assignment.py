# operator assignment/penugasan
# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment
""" # operator       contoh      sama dengan 
    1.  x            x = 5          x = 5
    2.  +=          x += 5          x = x + 5
    3.  -=          x -= 5          x = x - 5
    4.  *=          x *= 5          x = x * 5
    5.  /=          x /= 5          x = x / 5
    6.  %=          x %= 5          x = x % 5
    7.  //=         x //= 5         x = x // 5
    8.  **=         x **= 5         x = x ** 5 """


x = 5 #adalah assignmet
print('nilai x =', x)

x += 3
print('nilai x += 5, nilai x menjadi', x)    

x -= 3
print('nilai x -= 5, nilai x menjadi', x)    

x *= 3
print('nilai x *= 5, nilai x menjadi', x)    

x /= 3
print('nilai x /= 5, nilai x menjadi', x)    

x %= 3
print ('nilai x %= 5, nilai x menjadi', x)    

x //= 3
print('nilai x //= 5, nilai x menjadi', x)    

x **= 3
print('nilai x **= 5, nilai x menjadi', x)   

# operasi bitwise
# OR 
c = True
print("\nnilai c =",c)
c |= False
print('nilai c |= False, nilai c menjadi', c)
c = False
print("nilai c =",c)
c |= False
print('nilai c |= False, nilai c menjadi', c)

# AND 
c = True
print("\nnilai c =",c)
c &= False
print('nilai c &= False, nilai c menjadi', c)
c = False
print("nilai c =",c)
c &= True
print('nilai c &= False, nilai c menjadi', c)

# XOR 
c = True
print("\nnilai c =",c)
c ^= False
print('nilai c ^= False, nilai c menjadi', c)
c = True
print("nilai c =",c)
c ^= True
print('nilai c ^= False, nilai c menjadi', c)

#gese-geser
d = 0b0100
print("\nnilai d =",format(d,'04b'))
d >>= 2
print('nilai d >>= 2, nilai d menjadi',format(d,'04b'))
d <<= 1
print('nilai d <<= 2, nilai d menjadi',format(d,'04b'))
