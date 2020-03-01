import matplotlib.pyplot as plt
from skimage import io, transform
from scipy import ndimage
import numpy


fpath = '/store1/bypark/test_ComVis/1_transform/'
image = io.imread(fpath + 'cameraman.tif')
imageTranslated = numpy.zeros(numpy.shape(image))

# make transform x->x+15, y->y+30
Tx = 15
Ty = 30

T = [[1, 0, Tx],
     [0, 1, Ty],
     [0, 0, 1]]
T = numpy.linalg.inv(T)


# apply transform
iMax, jMax = numpy.shape(image)
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
