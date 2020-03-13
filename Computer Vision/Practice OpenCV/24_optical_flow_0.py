import cv2 as cv
import numpy as np

img0 = cv.imread('./image/optical-flow0.png')
img1 = cv.imread('./image/optical-flow1.png')

img0_gray = cv.cvtColor(img0, cv.COLOR_BGR2GRAY)
img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

# params for goodFeaturesToTrack
feature_params = dict(maxCorners = 100,
                      qualityLevel = 0.3,
                      minDistance = 7,    # 점들간에 거리는 최소 7은 되어야 한다.
                      blockSize = 7)


# 광흐름으로 추적하기 쉬운 강한 특징을 가진 점들을 선정
pts0 = cv.goodFeaturesToTrack(img0_gray, **feature_params)
# => pts0 = cv.goodFeaturesToTrack(img0_gray, maxCorners = 100, qualityLevel = 0.3, minDistance = 7, blockSize = 7)
print('pts0:', pts0.shape, pts0.dtype)  # 46개의 점을 찾음

lk_params = dict(winSize = (15,15),
                 maxLevel = 5,
                 criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

pts1, status, error = cv.calcOpticalFlowPyrLK(img0_gray, img1_gray, pts0, None, **lk_params)

print('pts1:', pts1.shape, pts1.dtype)
print('status:', status.shape, status.dtype)
print('error:', error.shape, error.dtype)

# Select only success points
pts0_success = pts0[status==1]
pts1_success = pts1[status==1]

print('p0_success :', pts0_success.shape, pts0_success.dtype)
print('p1_success :', pts1_success.shape, pts1_success.dtype)

for p in pts0_success:
    cv.circle(img0, tuple(p), 3, (255,0,0))

for p in pts1_success:
    cv.circle(img1, tuple(p), 3, (0,255,0))

cv.imshow('img0', img0)
cv.imshow('img1', img1)
cv.imshow('img0_gray', img0_gray)
cv.imshow('img1_gray', img1_gray)
cv.waitKey()