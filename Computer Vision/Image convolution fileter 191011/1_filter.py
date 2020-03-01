#과제
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
    #ConvImage (512, 512)
    KernelSizeI, KernelSizeJ = numpy.shape(kernel)
    #KernelSizeI = 3, KernelSizeJ = 3
    KernelRadius = int((KernelSizeI - 1)/2)
    #KernelRadius = 1
    img_pad = numpy.zeros((KernelSizeI, KernelSizeJ))
    img_pad = image
    for i in range(image.shape[1]-(KernelSizeI-1)):
        for j in range(image.shape[0]-(KernelSizeJ-1)):
            ker_pad = img_pad[i:i+KernelSizeI, j:j+KernelSizeJ]
            ConvImage[i][j] = (kernel*ker_pad).sum()

    return ConvImage.astype('uint8')

def medianFilter(image, kernel):
    ConvImage = numpy.zeros(numpy.shape(image))
    KernelRadius = int((kernel - 1) / 2)
    img_pad = numpy.zeros((image.shape[0] + KernelRadius + 1, image.shape[1] + KernelRadius + 1))
    img_pad[KernelRadius:-1, KernelRadius:-1] = image
    for i in range(image.shape[1]):
        for j in range(image.shape[0]):
            ker_pad = img_pad[j:j + kernel, i:i + kernel]
            ker_pad_1d = ker_pad.reshape(-1)
            ker_pad_1d.sort()

            ConvImage[j][i] = ker_pad_1d[len(ker_pad_1d) // 2]
    return ConvImage.astype('uint8')

PIXEL_MAX = 255
# Load image file
fpath = './'
image = io.imread(fpath + 'lena_gray.gif')

# make noise image
imageSaltAndPepper = util.noise.random_noise(image, mode='s&p')*PIXEL_MAX
imageSaltAndPepper = imageSaltAndPepper.astype('uint8')

# Kernel Definition
kernelSize = 5
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

ax = plt.subplot(1, 2, 1)
filteredImage = imageConvolution(imageSaltAndPepper, GaussianKernel) # Gaussian filtering
ax.imshow(filteredImage, cmap='gray')
plt.title('Gaussian Filtering')

ax = plt.subplot(1, 2, 2)
filteredImage = medianFilter(imageSaltAndPepper, 3) # Median filtering
ax.imshow(filteredImage, cmap='gray')
plt.title('Median Filtering')

plt.show()



