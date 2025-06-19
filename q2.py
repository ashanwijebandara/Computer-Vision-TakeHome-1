import cv2
import numpy as np

original = cv2.imread('OIP.jpg')
gray = cv2.imread('OIP.jpg', cv2.IMREAD_GRAYSCALE)

blur_3x3 = cv2.blur(gray, (3, 3))
blur_10x10 = cv2.blur(gray, (10, 10))
blur_20x20 = cv2.blur(gray, (20, 20))

blur_3x3 = cv2.cvtColor(blur_3x3, cv2.COLOR_GRAY2BGR)
blur_10x10 = cv2.cvtColor(blur_10x10, cv2.COLOR_GRAY2BGR)
blur_20x20 = cv2.cvtColor(blur_20x20, cv2.COLOR_GRAY2BGR)

size = (original.shape[1], original.shape[0])
blur_3x3 = cv2.resize(blur_3x3, size)
blur_10x10 = cv2.resize(blur_10x10, size)
blur_20x20 = cv2.resize(blur_20x20, size)

row1 = np.hstack((original, blur_3x3))
row2 = np.hstack((blur_10x10, blur_20x20))
grid = np.vstack((row1, row2))

cv2.imshow("Original | 3x3 | 10x10 | 20x20 (2x2 Grid)", grid)
cv2.waitKey(0)
cv2.destroyAllWindows()
