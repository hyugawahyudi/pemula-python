angka = 0

while angka < 5:
    print('nilai angka adalah :',angka)
    angka = angka + 1

print('diluar while')

Start = True #boolean
angka = 0
while Start:
    print('di dalam while ')
    if angka == 100:
        Start = False
        print('oke angka 100 ditemukan')
    angka += 1
