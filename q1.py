import cv2
import numpy as np

def reduce_intensity_levels(image_path, levels):
    # Ensure levels is a power of 2 and between 2 and 256
    if levels not in [2 ** i for i in range(1, 9)]:
        raise ValueError("Levels must be a power of 2 between 2 and 256")

    # Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError("Image not found. Please check the path.")

    # Calculate intensity interval
    factor = 256 // levels

    # Reduce intensity levels
    reduced_img = (img // factor) * factor

    return img, reduced_img


if __name__ == "__main__":
    try:
        #  Get image path from user
        image_path = input("Enter the path to the image: ").strip()

        #  Get number of intensity levels
        levels = int(input("Enter the number of intensity levels (power of 2 between 2 and 256): "))

        # Run the function
        original, reduced = reduce_intensity_levels(image_path, levels)

        # Display images
        cv2.imshow("Original Image", original)
        cv2.imshow(f"Reduced to {levels} Levels", reduced)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print("Error:", e)
