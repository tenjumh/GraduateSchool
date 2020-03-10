import cv2 as cv
import numpy as np

img = cv.imread('./image/edge_test1.jpg', cv.IMREAD_GRAYSCALE)
kernel1 = np.array([[-1, 0, 1],
                    [-1, 0, 1],
                    [-1, 0, 1]])

kernel2 = np.array([[-1, -1, -1],
                    [ 0,  0,  0],
                    [ 1,  1,  1]])

dst1 = cv.filter2D(img, cv.CV_32F, kernel1)
dst2 = cv.filter2D(img, cv.CV_32F, kernel2)

print(img.shape, img.dtype)
print(dst1, dst1.dtype)

print(dst2, dst2.dtype)

cv.imshow('original', img)
cv.imshow('dst1', dst1)
cv.imshow('dst1_abs', np.abs(dst1).astype(np.uint8))
cv.imshow('dst2', dst2)
cv.imshow('dst2_abs', np.abs(dst2).astype(np.uint8))
cv.waitKey()
