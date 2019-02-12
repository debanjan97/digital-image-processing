from convolute import Convolute
import numpy as np
import cv2

l = float(input("Enter the value of Lambda = "))
conv = Convolute("image.jpg", "GAUSS_BLUR")
image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
mask = conv.convolution()
image_final = image - mask
image_final = image + l*image_final
cv2.imwrite("unsharped_masked.jpg", image_final)
