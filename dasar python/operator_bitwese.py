# episode operator bitwise,operasi biner,binery

# bitwise adalah operasi masing" bit
""" int ==> 2 ==> 0 0 0 0 0 0 1 0
            index 7 6 5 4 3 2 1 0
                              2 dipangkatkan dengan index.2**1 = 2
     int ==> 1 ==> 0 0 0 0 0 0 0 1
             index 7 6 5 4 3 2 1 0
                                 2 dipangkan dengan index.2*0 = 1 
     int ==> 9 ==> 0 0 0 0 1 0 1 0
             index 7 6 5 4 3 2 1 0
                           2     2 dipangkan dengan index. 
                           8     1 terus dijumlahkan = 9 """

a = 9 
b = 5

# bitwise OR (|)
c = a | b
print ('\n =======OR=======')
print ('nilai :',a,',binary :',format(a,'08b'))
print ('nilai :',b,',binary :',format(b,'08b'))
print('--------------------------(|)')
print ('nilai :',c,',binary :',format(c,'08b'))

# bitwise AND (&)
c = a & b
print ('\n =======AND=======')
print ('nilai :',a,',binary :',format(a,'08b'))
print ('nilai :',b,',binary :',format(b,'08b'))
print('--------------------------(&)')
print ('nilai :',c,',binary :',format(c,'08b'))

# bitwise XOR (^)
c = a ^ b
print ('\n =======A XOR=======')
print ('nilai :',a,',binary :',format(a,'08b'))
print ('nilai :',b,',binary :',format(b,'08b'))
print('--------------------------(^)')
print ('nilai :',c,',binary :',format(c,'08b'))

# bitwise NOT (~)
c = ~a
print ('\n =======NOT=======')
print ('nilai :',a,',binary :',format(a,'08b'))
print('--------------------------(~)')
print ('nilai :',c,',binary :',format(c,'08b'))
print('--------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,',binary :',format(e^d,'08b'))

# shifting

# shif right(>>)
c = a >> 2
print('\n =========== >> ===========')
print ('nilai :',a,',binary :',format(a,'08b'))
print('--------------------------(>>)')
print ('nilai :',c,',binary :',format(c,'08b'))

# shif left(<<)
c = a << 2
print('\n =========== << ===========')
print ('nilai :',a,',binary :',format(a,'08b'))
print('--------------------------(<<)')
print ('nilai :',c,',binary :',format(c,'08b'))

