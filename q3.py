import cv2
import numpy as np

def rotate_image(image, angle):
    # Get image dimensions
    (h, w) = image.shape[:2]

    # Find the center of the image
    center = (w // 2, h // 2)

    # Create the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Compute the size of the output image to fit the whole rotated image
    cos = np.abs(rotation_matrix[0, 0])
    sin = np.abs(rotation_matrix[0, 1])
    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))

    # Adjust the rotation matrix to take into account translation
    rotation_matrix[0, 2] += (new_w / 2) - center[0]
    rotation_matrix[1, 2] += (new_h / 2) - center[1]

    # Rotate the image
    rotated = cv2.warpAffine(image, rotation_matrix, (new_w, new_h))
    return rotated

if __name__ == "__main__":
    try:
        path = input("Enter the path to the image: ").strip()
        image = cv2.imread(path)

        if image is None:
            raise FileNotFoundError("Image not found or path incorrect")

        # Rotate image
        rotated_45 = rotate_image(image, 45)
        rotated_90 = rotate_image(image, 90)

        # Show images
        cv2.imshow("Original Image", image)
        cv2.imshow("Rotated 45 Degrees", rotated_45)
        cv2.imshow("Rotated 90 Degrees", rotated_90)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print("Error:", e)
