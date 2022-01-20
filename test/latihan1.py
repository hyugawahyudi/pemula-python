print('===================================')
print
print('Data ke')
print('========== DATA MAHASISWA =========')
nama = input("masukkan nama     :")
nim = input("masukkann nim  :")
matkul = input("masukkan matkul     :")
uts = float(input("masukkan nilai uts   :"))
uas = float(input("masukkan nilai uas   :"))
nilai = (uts + uas)/2
print()
print('========== DATA MAHASISWA =========')
print("nama     :",nama)
print("nim      :",nim)
print("mata kuliah     :",matkul)
print("nilai rata - rata    :",nilai)

if 80 <= nilai <= 100 :
    print("Grade A")
elif 60 <= nilai <= 79 :
    print("Grade B")
elif 0 <= nilai <= 59 :
    print("Grade C")
else:
    print("ERROR")