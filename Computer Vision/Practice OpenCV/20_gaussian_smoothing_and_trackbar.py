import cv2 as cv
import numpy as np

img = cv.imread('./image/filter_blur.jpg')

def onChangedSigmaX(val):
    global sigma_x, sigma_y
    sigma_x = max(val, 0.01)   # 0일 때 에러가 나기에
    print('sigma_x, sigma_y =', sigma_x, sigma_y)
    img_blurred = cv.GaussianBlur(img, (0, 0), sigmaX=sigma_x, sigmaY=sigma_y)
    cv.imshow('img_blurred', img_blurred)

def onChangedSigmaY(val):
    global sigma_x, sigma_y
    sigma_y = max(val, 0.01) ㅋ
    print('sigma_x, sigma_y =', sigma_x, sigma_y)
    img_blurred = cv.GaussianBlur(img, (0, 0), sigmaX=sigma_x, sigmaY=sigma_y)
    cv.imshow('img_blurred', img_blurred)

sigma_x, sigma_y = 3, 3
cv.namedWindow('smoothed')
cv.createTrackbar('sigmax', 'smoothed', sigma_x, 10, onChangedSigmaX)
cv.createTrackbar('sigmay', 'smoothed', sigma_y, 10, onChangedSigmaY)

# (ry*2+1, rx*2+1) is kernel size in x and y direction
img_blurred = cv.GaussianBlur(img, (0, 0), sigmaX=sigma_x, sigmaY=sigma_y)
cv.imshow('img_blurred', cv.imshow('img_blurred', img_blurred))

cv.waitKey()