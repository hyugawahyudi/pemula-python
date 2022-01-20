# scop variabel : local 

namaKucing ='Tom cat'

def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru
    print('saya rubah nama kucing menjadi',namaKucing)

rubahNamaKucing('ketie')
print('nama kucing saya menjadi',namaKucing)

print("="*35)
# scop variabel : global 

namaKucing = 'Tom cat'
makananKucing = 'royal canin'

def rubahNamaKucing(namaBaru):
    global namaKucing # variabel global
    namaKucing = namaBaru # varibel local
    print('saya rubah nama kucing menjadi',namaKucing)

def kasihMakanKucing(makanan,nama):
    global namaKucing,makananKucing
    namaKucing = nama
    makananKucing = makanan

rubahNamaKucing('ketie')
kasihMakanKucing('universal','alek')
print('nama kucing saya menjadi',namaKucing,'dan makan',makananKucing)