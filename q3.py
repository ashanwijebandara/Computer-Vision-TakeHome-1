import cv2
import numpy as np

image = cv2.imread('OIP.jpg')
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M45 = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_45 = cv2.warpAffine(image, M45, (w, h), borderMode=cv2.BORDER_REPLICATE)
rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
target_height = 300
def resize_to_height(img, height):
    h, w = img.shape[:2]
    new_w = int(w * (height / h))
    return cv2.resize(img, (new_w, height))

image_resized = resize_to_height(image, target_height)
rotated_45_resized = resize_to_height(rotated_45, target_height)
rotated_90_resized = resize_to_height(rotated_90, target_height)
combined = np.hstack((image_resized, rotated_45_resized, rotated_90_resized))

cv2.imshow("Original | Rotated 45° | Rotated 90°", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
