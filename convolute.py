import cv2
import numpy as np
from copy import deepcopy

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
#negative
image_negative = deepcopy(image)
for x in range(len(image)):
    for y in range(len(image[0])):
        image_negative[x][y] = 255 -  image[x][y]
cv2.imwrite("image_neg.jpg",image_negative)
#cv2.waitKey(10000)
kernel_size = 7
padded_image = np.zeros((kernel_size - 1 + len(image), kernel_size - 1 + len(image[0])))
for x in range(len(image)):
    for y in range(len(image[0])):
        padded_image[int(kernel_size/2) + x][int(kernel_size/2) + y] = image_negative[x][y]

kernel = np.full((kernel_size, kernel_size), 1)

mod_image = np.zeros((len(image), len(image[0])))



for i in range(len(image)):
    for j in range(len(image[0])):
        val = 0
        for x in range(-1*int((kernel_size-1)/2), int((kernel_size-1)/2) + 1):
            for y in range(-int((kernel_size-1)/2), int((kernel_size-1)/2) + 1):
                val += padded_image[x + i][y + j]*kernel[x][y]
        val /= kernel_size**2
        mod_image[i][j] = val
cv2.imwrite("image_conv.jpg",mod_image)
