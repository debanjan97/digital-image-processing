import numpy as np

class Kernel:
    def __init__(self, type):
        self.type = type
        self.matrix = np.zeros((3,3))
        if self.type == "IDENTITY":
            self.matrix[1][1] = 1
        elif self.type == "EDGE_DETECTION1":
            self.matrix[0][0] = 1
            self.matrix[0][2] = -1
            self.matrix[2][0] = -1
            self.matrix[2][2] = 1
        elif self.type == "EDGE_DETECTION2":
            self.matrix[0][1] = 1
            self.matrix[1][0] = 1
            self.matrix[1][1] = -4
            self.matrix[1][2] = 1
            self.matrix[2][1] = 1
        elif self.type == "EDGE_DETECTION3":
            self.matrix = np.full((3,3), -1)
            self.matrix[1][1] = 8
        elif self.type == "SHARPEN":
            self.matrix[0][1] = -1
            self.matrix[1][0] = -1
            self.matrix[1][1] = 4
            self.matrix[1][2] = -1
            self.matrix[2][1] = -1
        elif self.type == "BOX":
            self.matrix = np.full((3,3), 1/9)
        elif self.type == "GAUSS_BLUR":
            self.matrix = np.full((3,3), 1/16)
            self.matrix[0][1] = 2/16
            self.matrix[1][0] = 2/16
            self.matrix[1][1] = 4/16
            self.matrix[1][2] = 2/16
            self.matrix[2][1] = 2/16

    def getKernel(self):
        return self.matrix
