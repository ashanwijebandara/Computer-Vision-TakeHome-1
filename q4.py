import cv2
import numpy as np

def blockwise_average(img, block_size):
    h, w = img.shape
    result = img.copy()

    for i in range(0, h - block_size + 1, block_size):
        for j in range(0, w - block_size + 1, block_size):
            # Extract the block
            block = img[i:i + block_size, j:j + block_size]
            # Compute average
            avg = int(np.mean(block))
            # Set all values in block to average
            result[i:i + block_size, j:j + block_size] = avg

    return result

if __name__ == "__main__":
    try:
        # Input image path
        path = input("Enter the path to a grayscale image: ").strip()
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            raise FileNotFoundError("Image not found. Please check the path.")

        # Apply block-wise averaging
        block3 = blockwise_average(img, 3)
        block5 = blockwise_average(img, 5)
        block7 = blockwise_average(img, 7)

        # Show results
        cv2.imshow("Original Image", img)
        cv2.imshow("3x3 Block Averaged", block3)
        cv2.imshow("5x5 Block Averaged", block5)
        cv2.imshow("7x7 Block Averaged", block7)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print("Error:", e)
