import cv2 as cv
import numpy as np

img = cv.imread('./image/filter_blur.jpg')
kernel = np.array([[0,-1,0],
                   [-1,5,-1],
                   [0,-1,0]])

img_filtered = cv.filter2D(img, -1, kernel)

print(img.shape, img.dtype)
print(img_filtered, img_filtered.dtype)

cv.imshow('original', img)
cv.imshow('filtered', img_filtered)
cv.waitKey()