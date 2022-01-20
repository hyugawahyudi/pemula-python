# nilai = 50

# if nilai == 60: # equal eksplisit
#     print("nilai anda :", nilai)

# if nilai != 60:
#     print("nilai anda :",nilai)

# if nilai is 60: # equal
#     print("nilai anda :",nilai)

# if nilai is not 60: # not equal
#     print("nilai anda :",nilai)

# print('='*20)

# nilai = 30

# if 80 <= nilai <= 100:
#     print('nilai anda adalah A')
# elif 70 <= nilai < 80:
#     print('nilai anda adalah B')
# elif 60 <= nilai < 70:
#     print('nilai anda adalah C')
# elif 50 <= nilai < 60:
#     print('nilai anda adalah D, lakukan perbaikan')
# else:
#     prints('maaf anda tidak lulus matakuliah ini')

print('='*30)
print('operator logika untuk list dan string')
print('')

gorengan = ["bakwan","cireng","pisang goreng","pukis","mie ayam"]
beli = "bakso"

if beli in gorengan:
    print('mamang bilang, "ya, saya jual',beli,'"')
if not beli in gorengan:
    print('"saya gak jual',beli,'"')

karakter = 'k'
if karakter in beli:
    print("ada",karakter,"di",beli)
else:
    print("tida ada",karakter,"di",beli)
