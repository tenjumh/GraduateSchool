import matplotlib.pyplot as plt
from skimage import io, filters, util, morphology, measure
import numpy
from scipy import signal
import math

def gkern(kernlen, nsig):
    # Return 2D Gaussian Kernel
    gkern1d = signal.gaussian(kernlen, std=nsig).reshape(kernlen, 1)
    kernel = numpy.outer(gkern1d, gkern1d)

    return kernel/kernel.sum()


def imageConvolution(image,kernel):

    ConvImage = numpy.zeros(numpy.shape(image))
    KernelSizeI, KernelSizeJ = numpy.shape(kernel)
    KernelRadius = int((KernelSizeI - 1)/2)

    iMax, jMax = numpy.shape(image)
    i = KernelRadius
    while i < iMax - KernelRadius:
        j = KernelRadius
        while j < jMax - KernelRadius:
            # convolution operation
            ConvImage[i, j] = numpy.multiply(image[i-KernelRadius:i+KernelRadius+1, j-KernelRadius:j+KernelRadius+1], kernel).sum()

            j = j + 1

        i = i + 1

    return ConvImage.astype('uint8')


PIXEL_MAX = 255
# Load image file
fpath = '/store1/bypark/test_ComVis/2_filter/'
image = io.imread(fpath + 'lena_gray.gif')


# make noise image
imageSaltAndPepper = util.noise.random_noise(image, mode='s&p')*PIXEL_MAX
imageSaltAndPepper = imageSaltAndPepper.astype('uint8')

# Kernel Definition
kernelSize = 3
sigma = 3
GaussianKernel = gkern(kernelSize, sigma)
MedianFilterWindow = morphology.square(kernelSize)

# Original Image
ax = plt.subplot(3, 2, 1)
ax.imshow(image, cmap='gray')
plt.title('Original Image')

# Salt & Pepper Noise Reduction
ax = plt.subplot(3, 2, 2)
ax.imshow(imageSaltAndPepper, cmap='gray')
plt.title('Gaussian Noise')

ax = plt.subplot(3, 2, 4)
filteredImage = imageConvolution(imageSaltAndPepper, GaussianKernel)
ax.imshow(filteredImage, cmap='gray')
plt.title('Gaussian Filtering')

ax = plt.subplot(3, 2, 6)
filteredImage = filters.median(imageSaltAndPepper, MedianFilterWindow)
ax.imshow(filteredImage, cmap='gray')
plt.title('Median Filtering')


plt.show()
