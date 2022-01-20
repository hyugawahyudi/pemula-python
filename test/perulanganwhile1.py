print("\n======= WHILE ========")

total = 0
jumlah = 0
stop = False

while stop == False:
    angka = input('masukkan angka :')

    if angka =="":
        stop = True
    else:
        angka = float (angka)
        total += angka
        jumlah += 1

print(total)
print(jumlah)

rata_rata = total / jumlah
print(rata_rata)
