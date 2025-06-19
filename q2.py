import cv2

def apply_average_blur(image_path):
    # Load the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError("Image not found. Please check the path.")

    # Apply average filters with different kernel sizes
    blur_3x3 = cv2.blur(img, (3, 3))
    blur_10x10 = cv2.blur(img, (10, 10))
    blur_20x20 = cv2.blur(img, (20, 20))

    # Display original and blurred images
    cv2.imshow("Original Image", img)
    cv2.imshow("3x3 Average Filter", blur_3x3)
    cv2.imshow("10x10 Average Filter", blur_10x10)
    cv2.imshow("20x20 Average Filter", blur_20x20)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        # Get image path from user
        path = input("Enter the path to the image: ").strip()
        apply_average_blur(path)

    except Exception as e:
        print("Error:", e)
