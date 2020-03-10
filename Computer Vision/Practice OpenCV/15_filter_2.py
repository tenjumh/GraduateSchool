import cv2 as cv
import numpy as np

img = cv.imread('./image/edge_test.jpg', cv.IMREAD_GRAYSCALE)
kernel1 = np.array([[-1,0,0],
                   [0,1,0],
                   [0,0,0]])

kernel2 = np.array([[0,0,-1],
                   [0,1,0],
                   [0,0,0]])

dst1 = cv.filter2D(img, cv.CV_32F, kernel1)
dst2 = cv.filter2D(img, cv.CV_32F, kernel2)

print(img.shape, img.dtype)
print(dst1, dst1.dtype)
print(dst2, dst2.dtype)

cv.imshow('original', img)
cv.imshow('dst1', dst1)
cv.imshow('dst2', dst2)
cv.waitKey()
