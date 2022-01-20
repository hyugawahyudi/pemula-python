""" perulangan for
1. mengulang blok statemen dengan jumlah perulangan yanga sudah ditentukan.
2. menggunakan fungsin range() untuk menentukan jumlah perulangan.
3. 3 bentuk range () 
    * range (n) = melakukan perulangan dari 0 sampei (n-1).
    * range (m,n) = melakukan perulangan dari m sampai (n-1).
    * range (m,n,i) = melakukan perulangan dari m sampai (n-1) dengan nilai penambahan
                    (increment) = i.
contoh =
    * range (6) = 0,1,2,3,4,5
    * range (2,6) = 2,3,4,5
    * range (2,6,2) = 2,4
4. for juga bisa menggunakan statement continue,break dan else. """


for i in range (6) :
    print(i)

for j in range (2,6):
    print(j)

for k in range (2,6,2) :
    print(k)