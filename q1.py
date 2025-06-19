import cv2
import numpy as np

# Input from user
levels = int(input("Enter the number of intensity levels (power of 2 between 2 and 256): "))

original = cv2.imread('OIP.jpg')
gray = cv2.imread('OIP.jpg', cv2.IMREAD_GRAYSCALE)

factor = 256 // levels
reduced = (gray // factor) * factor

reduced_bgr = cv2.cvtColor(reduced, cv2.COLOR_GRAY2BGR)

if original.shape != reduced_bgr.shape:
    reduced_bgr = cv2.resize(reduced_bgr, (original.shape[1], original.shape[0]))

combined = np.hstack((original, reduced_bgr))
cv2.imshow(f"Original (Left) | Reduced to {levels} Levels (Right)", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
