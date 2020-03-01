import matplotlib.pyplot as plt
from skimage import io, transform
import scipy
from scipy import ndimage
import numpy
import math


fpath = '/store1/bypark/test_ComVis/1_transform/'
image = io.imread(fpath + 'cameraman.tif')
imageTranslated = numpy.zeros(numpy.shape(image))

# make transform Translation -> Rotation -> Translation
iMax, jMax = numpy.shape(image)

Tx = - (0 + (iMax-1)) / 2
Ty = - (0 + (jMax-1)) / 2
Translation = \
    [[1, 0, Tx],
     [0, 1, Ty],
     [0, 0, 1]]


Theta = math.radians(30)
Rotation = \
    [[math.cos(Theta), -math.sin(Theta), 0],
     [math.sin(Theta), math.cos(Theta), 0],
     [0, 0, 1]]


T = numpy.dot(numpy.linalg.inv(Translation), numpy.dot(Rotation, Translation))
T = numpy.linalg.inv(T)


# apply transform
iTranslated = 0
while iTranslated < iMax:

    jTranslated = 0
    while jTranslated < jMax:

        nativeI, nativeJ, temp = numpy.dot(T, numpy.transpose([iTranslated, jTranslated, 1]))
        imageTranslated[iTranslated, jTranslated] = ndimage.map_coordinates(image, [[nativeI], [nativeJ]], order=1)

        jTranslated = jTranslated + 1
    iTranslated = iTranslated + 1

# Check result
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.imshow(imageTranslated, cmap='gray')
plt.show()
