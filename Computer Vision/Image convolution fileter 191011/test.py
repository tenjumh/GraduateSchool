import matplotlib.pyplot as plt
from skimage import io, filters, util, morphology, measure
import numpy
from scipy import signal
import math

PIXEL_MAX = 255
# Load image file
fpath = './'
image = io.imread(fpath + 'lena_gray.gif')

def gkern(kernlen, nsig):
    # Return 2D Gaussian Kernel
    gkern1d = signal.gaussian(kernlen, std=nsig).reshape(kernlen, 1)
    kernel = numpy.outer(gkern1d, gkern1d)
    return kernel/kernel.sum()

# make noise image
imageSaltAndPepper = util.noise.random_noise(image, mode='s&p')*PIXEL_MAX
imageSaltAndPepper = imageSaltAndPepper.astype('uint8')

# Kernel Definition
kernelSize = 3
sigma = 3
GaussianKernel = gkern(kernelSize, sigma)
MedianFilterWindow = morphology.square(kernelSize)

ConvImage = numpy.zeros(numpy.shape(image))
#ConvImage (512, 512)
KernelSizeI, KernelSizeJ = numpy.shape(GaussianKernel)
#KernelSizeI = 3, KernelSizeJ = 3
KernelRadius = int((KernelSizeI - 1)/2)
#KernelRadius = 1
img_pad = numpy.zeros((KernelSizeI, KernelSizeJ))
img_pad = image
for i in range(image.shape[1]-(KernelSizeI-1)):
    for j in range(image.shape[0]-(KernelSizeJ-1)):
        ker_pad = img_pad[i:i+KernelSizeI, j:j+KernelSizeJ]
        #ker_pad_m = ker_pad
        #ker_pad_m = ker_pad_m.reshape(-1)
        #print(ker_pad.shape)
        ConvImage[i][j] = (GaussianKernel*ker_pad).sum()
        #print(ConvImage[j][i])
        ConvImage.astype('uint8')
print(ker_pad)

#ConvImage
#plt.imshow(ConvImage, cmap='gray')
#plt.title('Gaussian Filtering')