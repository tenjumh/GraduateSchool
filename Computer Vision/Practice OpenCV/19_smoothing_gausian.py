import cv2 as cv
import numpy as np

img = cv.imread('./image/filter_blur.jpg')

rx, ry = 12, 6   # 커널 반지름 사이즈
sx, sy = 4, 2  # spread of Gauussian in x and y direction

kernel = np.zeros((ry*2+1, rx*2+1), np.float32)
for i in range(kernel.shape[0]):
    for j in range(kernel.shape[1]):
        x = j - rx  # x distance from the kernel center
        y = i - ry  # y distance from the kernel center
        kernel[i,j] = np.exp(-(x*x)/(2*sx*sx)-(y*y)/(2*sy*sy))

cv.imshow('kernel', cv.resize(kernel, (300, 200)))
print('kernel.sum() =', kernel.sum())
kernel /= kernel.sum()  # make the kernel sum 0
img_smoothed = cv.filter2D(img, -1, kernel)
cv.imshow('img_smoothed', img_smoothed)

# (ry*2+1, rx*2+1) is kernel size in x and y direction
img_blurred = cv.GaussianBlur(img, (ry*2+1, rx*2+1), sigmaX=sx, sigmaY=sy)
cv.imshow('img_blurred', img_blurred)

# autosigma
img_blurred_autosigma = cv.GaussianBlur(img, (ry*2+1, rx*2+1), 0)

cv.imshow('img_blurred_autosigma', img_blurred_autosigma)

cv.imshow('original', img)
cv.waitKey()