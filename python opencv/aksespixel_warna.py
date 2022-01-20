import cv2 as cv



citra = cv.imread("bunga.jpeg")

print(citra.shape)

jumlahBaris = citra.shape[0]
jumlahKolom = citra.shape[1]

citra2 = citra.copy()

for b in range(0,jumlahBaris):
    for k in range(0,jumlahKolom):
        blue, green, red = citra[b, k]
        citra2[b, k] = blue + 30, green + 30, red + 30

cv.imwrite("citra2.jpeg",citra2)