# if multi kondisi (AND dan OR) 

nilai1 = int(input("masukkan nilai1 :"))
nilai2 = int(input("masukkan nilai2 :"))

if nilai1 >= 60 and nilai2 >= 60 :
    print("semua nilai lulus")
elif nilai1 >= 60 or nilai2 >= 60 :
    print("hanya 1 nilai yang lulus")
else:
    print("tidak ada yang lulus")

# statement pass 
a = 10
if a < 10 :
     print("benar")
else:
    pass

# ternary
a = 7
b = 10

print("nilai variabel terbesar :")
print("a") if a > b else print("b")
