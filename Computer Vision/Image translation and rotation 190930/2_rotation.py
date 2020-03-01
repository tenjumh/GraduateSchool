import matplotlib.pyplot as plt
from skimage import io, transform
import scipy
from scipy import ndimage
import numpy as np
import math

fpath = './'
image = io.imread(fpath + 'cameraman.tif')
imageTranslated = np.zeros(np.shape(image))

# make transform Translation -> Rotation -> Translation
iMax, jMax = np.shape(image)

Tx = - (0 + (iMax-1)) / 2
Ty = - (0 + (jMax-1)) / 2
Translation = np.array([[1, 0, 0], [0, 1, 0], [Tx, Ty, 1]]) # Transform matrix for translation


Theta = math.radians(30)
Rotation = np.array([[math.cos(Theta), math.sin(Theta), 0], [-math.sin(Theta), math.cos(Theta), 0], [0, 0, 1]]) # Transform matrix for rotation

T = np.array([[1, 0, 0], [0, 1, 0], [-Tx, -Ty, 1]]) # Transformation matrix
#T = numpy.linalg.inv(T)

# apply transform
iTranslated = 0
while iTranslated < iMax:

    jTranslated = 0
    while jTranslated < jMax:

        pixel_data = image[iTranslated, jTranslated]
        input_coords = np.array([iTranslated, jTranslated, 1])
        trans_coords = np.dot(input_coords, Translation)
        rota_coords = np.dot(trans_coords, Rotation)
        i_out, j_out, _ = np.dot(rota_coords, T)
        if i_out < 256 and i_out > 0 and j_out < 256 and j_out > 0:
            imageTranslated[int(i_out), int(j_out)] = pixel_data
            #imageTranslated[i_out, j_out] = pixel_data

        jTranslated = jTranslated + 1
    iTranslated = iTranslated + 1

# Check result
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.imshow(imageTranslated, cmap='gray')
plt.show()
