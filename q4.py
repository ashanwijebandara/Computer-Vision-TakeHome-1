import cv2
import numpy as np

def blockwise_average(img, block_size):
    h, w = img.shape
    result = img.copy()
    for i in range(0, h - block_size + 1, block_size):
        for j in range(0, w - block_size + 1, block_size):
            block = img[i:i + block_size, j:j + block_size]
            avg = int(np.mean(block))
            result[i:i + block_size, j:j + block_size] = avg
    return result

image = cv2.imread('OIP.jpg')
img = cv2.imread("OIP.jpg", cv2.IMREAD_GRAYSCALE)
block3 = blockwise_average(img, 3)
block5 = blockwise_average(img, 5)
block7 = blockwise_average(img, 7)
block3 = cv2.cvtColor(block3, cv2.COLOR_GRAY2BGR)
block5 = cv2.cvtColor(block5, cv2.COLOR_GRAY2BGR)
block7 = cv2.cvtColor(block7, cv2.COLOR_GRAY2BGR)
size = (360, 360)
image = cv2.resize(image, size)
block3 = cv2.resize(block3, size)
block5 = cv2.resize(block5, size)
block7 = cv2.resize(block7, size)
top_row = np.hstack((image, block3))
bottom_row = np.hstack((block5, block7))
grid = np.vstack((top_row, bottom_row))

cv2.imshow("2x2 Blockwise Averaging: Original | 3x3 | 5x5 | 7x7", grid)
cv2.waitKey(0)
cv2.destroyAllWindows()
