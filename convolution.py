from kernel import Kernel
import numpy as np
import cv2

print("Choose from the following:\n IDENTITY \t EDGE_DETECTION1/2/3 \t BOX \t GAUSS_BLUR\n SHARPEN")
response = input()

if response not in ["IDENTITY", "EDGE_DETECTION1", "EDGE_DETECTION2", "EDGE_DETECTION3", "BOX", "GAUSS_BLUR", "SHARPEN"]:
    print("Enter the right response next time :)")
    exit()

kernel = Kernel(response)
kernel = kernel.getKernel()
kernel_size = 3

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("OGimage.jpg", image)
padded_image = np.zeros((kernel_size - 1 + len(image), kernel_size - 1 + len(image[0])))
for x in range(len(image)):
    for y in range(len(image[0])):
        padded_image[int(kernel_size/2) + x][int(kernel_size/2) + y] = image[x][y]


mod_image = np.zeros((len(image), len(image[0])))



for i in range(len(image)):
    for j in range(len(image[0])):
        val = 0
        for x in range(-1*int((kernel_size-1)/2), int((kernel_size-1)/2) + 1):
            for y in range(-int((kernel_size-1)/2), int((kernel_size-1)/2) + 1):
                val += padded_image[x + i][y + j]*kernel[x][y]
        mod_image[i][j] = val
cv2.imwrite("{}.jpg".format(response),mod_image)
