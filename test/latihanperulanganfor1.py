angka1 = float(input("input angka 1 :"))
angka2 = float(input("input angka 2 :"))
angka3 = float(input("input angka 3 :"))

rata2 = (angka1 + angka2 + angka3) / 3
print(rata2)

print("\n======= FOR ========")

total = 0
jumlah = 0

for i in range (0,5) :
    angka = float(input("input angka :"))

    total += angka
    jumlah += 1
    
print(total)
print(jumlah)

rata2 = total / jumlah
print (rata2)