import cv2
from kernel import Kernel
import numpy as np

class Convolute:
    def __init__(self, image_name, kernel_type):
        self.image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
        self.kernel = Kernel(kernel_type)
        self.kernel = self.kernel.getKernel()
        self.kernel_size = 3
        self.type = kernel_type

    def convolution(self):
        padded_image = np.zeros((self.kernel_size - 1 + len(self.image), self.kernel_size - 1 + len(self.image[0])))
        for x in range(len(self.image)):
            for y in range(len(self.image[0])):
                padded_image[int(self.kernel_size/2) + x][int(self.kernel_size/2) + y] = self.image[x][y]

        mod_image = np.zeros((len(self.image), len(self.image[0])))
        for i in range(len(self.image)):
            for j in range(len(self.image[0])):
                val = 0
                for x in range(-1*int((self.kernel_size-1)/2), int((self.kernel_size-1)/2) + 1):
                    for y in range(-int((self.kernel_size-1)/2), int((self.kernel_size-1)/2) + 1):
                        val += padded_image[x + i][y + j]*self.kernel[x][y]
                mod_image[i][j] = val
        cv2.imwrite("{}.jpg".format(self.type),mod_image)

if __name__ == "__main__":
    print("Choose from the following:\n IDENTITY \t EDGE_DETECTION1/2/3 \t BOX \t GAUSS_BLUR\n SHARPEN")
    response = input()
    if response not in ["IDENTITY", "EDGE_DETECTION1", "EDGE_DETECTION2", "EDGE_DETECTION3", "BOX", "GAUSS_BLUR", "SHARPEN"]:
        print("Enter the right response next time :)")
        exit()

    yo = Convolute("image.jpg", response)
    yo.convolution()
