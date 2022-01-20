import cv2 as cv

citra = cv.imread("bunga.jpeg")
# print(citra[0,0])
# B G R 

citra[0,0] = [0,0,0]

# cv.imwrite("hasil.jpeg",citra)

citraAbu = cv.cvtColor(citra,cv.COLOR_BGR2GRAY)
print(citraAbu[10,10])

citraAbu[10,10] = 255
cv.imwrite ("citraAbu.jpeg",citraAbu)