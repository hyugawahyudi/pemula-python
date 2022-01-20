print("===> APLIKASI MENGHUTUNG GAJI KARYAWAN")

nim = int(input         ("NIM           :"))
nama = input        ("Nama          :")
gol = input         ("Golongan      :")
jikabenar = True
if gol == '1' :
    gaji_pokok = 2000000
elif gol == '2' :
    gaji_pokok = 3000000
elif gol == '3' :
    gaji_pokok = 4000000
elif gol == '4' :
    gaji_pokok = 5000000
else:
    jikabenar = False
    print("MAAF, GOLONGAN YANG DIINPUTKAN (1-4)")

if jikabenar == True :
    jml_anak = int(input("Jumlah Anak   :"))
if jml_anak == 0 :
    tunjangan = 0
elif jml_anak == 1 :
    tunjangan = 250000
elif jml_anak == 2 :
    tunjangan = 350000
elif jml_anak == 3 :
    tunjangan = 450000
elif jml_anak == 4 :
    tunjangan = 550000
else:
    jikabenar = False
    print("MAAF, JUMLAH ANAK YANG DI INPUTKAN SALAH")

if jikabenar == True :
    print("--------PT CINTA--------")
    print("------------------------")
    print("------JALAN SETIA-------")
    print("NIM              :",nim)
    print("NAMA KARYAWAN    :",nama)
    print("GOLONGAN         :",gol)
    print("Jumlah Anak      :",jml_anak)
    print("Gaji Pokok       :", gaji_pokok)
    print("Tunjangan        :",tunjangan) 
    print("=======================")
    print("Gaji Bersih","Rp.", gaji_pokok + tunjangan,",00")
    print("=======================")