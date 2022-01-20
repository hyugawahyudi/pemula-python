import cv2 as cv

citra = cv.imread ("bunga.jpeg",cv.IMREAD_GRAYSCALE)
cv.imshow("gambar",citra)
cv.waitKey(0)