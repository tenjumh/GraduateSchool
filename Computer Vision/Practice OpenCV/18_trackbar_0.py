# trackbar를 통해 색을 변화시켜보자

import cv2
import numpy as np
'''
흑백이미지
def onChange(val):
    pos = cv2.getTrackbarPos('brightness', 'img')
    print(val, pos)
    img.fill(val)
    cv2.imshow('img', img)

init_val = 128
img = np.full((480, 640), init_val, np.uint8)
cv2.namedWindow('img')
cv2.createTrackbar('brightness', 'img', init_val, 255, onChange)
'''
def onChangeR(val):
    #pos = cv2.getTrackbarPos('R', 'img')
    print('R:', val)
    img[:,:,2] = val
    cv2.imshow('img', img)

def onChangeG(val):
    #pos = cv2.getTrackbarPos('G', 'img')
    print('G:', val)
    img[:,:,1] = val
    cv2.imshow('img', img)

def onChangeB(val):
    #pos = cv2.getTrackbarPos('B', 'img')
    print('B:', val)
    img[:,:,0] = val
    cv2.imshow('img', img)

init_val = 255
img = np.full((480, 640, 3), init_val, np.uint8)
cv2.namedWindow('img')
cv2.createTrackbar('R', 'img', init_val, 255, onChangeR)  # onChange : callback 함수
cv2.createTrackbar('G', 'img', init_val, 255, onChangeG)
cv2.createTrackbar('B', 'img', init_val, 255, onChangeB)

print(img.shape)
cv2.imshow('img', img)
cv2.waitKey()