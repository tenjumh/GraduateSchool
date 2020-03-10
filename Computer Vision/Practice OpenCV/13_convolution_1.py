# blur gray image

import cv2 as cv
import numpy as np

def filter_gray(img, kernel):
    kh, kw = kernel.shape[0:2]
    kh2, kw2 = kh//2, kw//2

    tmp_shape = list(img.shape)
    tmp_shape[0] += kh2*2  # height
    tmp_shape[1] += kw2*2  # width

    tmp = np.zeros(tmp_shape, img.dtype)
    np.copyto(tmp[kh2:kh2+img.shape[0], kw2:kw2+img.shape[1]], img)
    dst = np.zeros(img.shape, img.dtype)

    for i in range(dst.shape[0]):
        for j in range(dst.shape[1]):
            dst[i, j] = (tmp[i:i+kh, j:j+kw]*kernel).sum()

    return dst

img = cv.imread('./image/filter_blur.jpg', cv.IMREAD_GRAYSCALE)
ksize = 9

# 1/9(3 by 3)
kernel = np.full((ksize, ksize), 1./(ksize*ksize))
img_filtered = filter_gray(img, kernel)

cv.imshow('original', img)
cv.imshow('blur', img_filtered)
cv.waitKey(0)