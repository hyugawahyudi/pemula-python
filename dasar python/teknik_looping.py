# teknik looping

nama_band = [
    'Payung twdung',
    'Fourtwnty',
    'Dialog Dini Hari',
    'Mr.Sonjaya',
    'Parahyena',
    'Syahrini']

kumpulan_lagu = [
    'Akad',
    'Zona Nyaman',
    'Rumahku',
    'Sang Filsuf',
    'Sindoro',
    'Jodohku']

# iterasi = 0
# for band in nama_band:
#     print('no:',iterasi,'nama band',band)
#     iterasi += 1

# enumerate
for index,band in enumerate (nama_band):
    print(index,':',band)

# zip (menyatukan)
for band,lagu in zip(nama_band,kumpulan_lagu): # 2 ini kayak di pasang pasangin tapi korespondennya satu satu.
    print(band,'menyanyikan lagu yang berjadul :',lagu) #kalau tidak ada temannya dia tidak dimunculkan

# set 
playlist ={'baby baby','ada apa dengan cinta','cenat cenut','jaran goyang','gorgom','kuda','kucing'}

for lagu in sorted(playlist):
    print(lagu)

# dictionary

print('='*35)

playlist2 = {
    'Payung twdung': 'akad',
    'Fourtwnty': 'zona nyaman',
    'Dialog Dini Hari': 'Rumahku'
    }

for i in playlist2.keys(): # kalau mengambil kucinya pake keys
    print(i)
for i in playlist2.values():# kalau mengambil datanya pake values
    print(i)
for i,v in playlist2.items():# kalau mengambil dua duanya pake items
    print(i,'lagunya:',v)

# reversed (kalau mau di balek)
for i in reversed(range(1,10,1)):
    print(i)