import cv2 as cv

citraAbu = cv.imread("bunga.jpeg",cv.IMREAD_GRAYSCALE)

print(citraAbu.shape)

jumlahKolom = citraAbu.shape[1]
jumlahBaris = citraAbu.shape[0]

citraAbu2 = citraAbu.copy()

for b in range(0,jumlahBaris):
    for k in range(0,jumlahKolom):
        intensitas = citraAbu[b, k]
        citraAbu[b, k] = intensitas + 30

cv.imwrite("citraAbu.jpeg",citraAbu)
cv.imwrite("citraAbu2.jpeg",citraAbu2)