# print("a", end="")
# print("b")

angka = int(input("inputkan angka :"))

for i in range (1,angka + 1) :
    for j in range (1, angka + 1):
        print("*",end= "")
    print("")
 
print("="*20)

for i in range (1,angka + 1) :
    for j in range (i):
        print("*",end= "")
    print("")

print("="*20)

for i in range (angka,0, -1) :
    for j in range (i):
        print("*",end= "")
    print("")
