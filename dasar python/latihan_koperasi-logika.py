# # operasi latihan logika dan komparasi 

# # membuat gabungan area rentang dari angka

# # ++++++++3----------10+++++++++

# InputUser = float(input('masukkan angka yang bernilai\nkurang dari 3\natau \nlebih dari 10\n :'))

# # ++++++++3----------
# # memeriksa angka kurang dari 3
# isKurangDari = (InputUser < 3)
# print("Kurang dari 3 =",isKurangDari)

# # ----------10+++++++++++
# # memeriksa angka dari 10
# isLebihDari = (InputUser > 10)
# print("lebih dari 10 =",isLebihDari)

# # ++++++3---------10++++++

# isCorrect = isKurangDari or isLebihDari
# print("anda yang akan ada masukkan :",isCorrect)

# # ------3+++++++10-------
# # kasus irisan
# print("\n",10*"=","\n")
# InputUser = float(input('masukkan angka yang bernilai\n lebih dari 3\natau \n kurang dari 10\n :'))

# #-------3++++++++++
# # lebih dari 3
# isKurangDari = (InputUser > 3)
# print("Kurang dari 3 =",isKurangDari)

# # +++++++++++10--------
# # kurang dari 10
# isLebihDari = (InputUser < 10)
# print("lebih dari 10 =",isLebihDari)

# # -------3+++++++++10---------

# isCorrect = isKurangDari and isLebihDari
# print("anda yang akan ada masukkan :",isCorrect)

Data = float(input("Masukkan angka :"))
if (Data > 0 and Data < 5) or ( Data > 8 and Data < 11) :
    print("True")
else :
    print("False")