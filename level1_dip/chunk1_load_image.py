from pathlib import Path

import cv2

# Load the image next to this script so the program works from any working directory.
image_path = Path(__file__).with_name("test_img.jpg")
img = cv2.imread(str(image_path))
if img is None:
	raise FileNotFoundError(f"Could not load image: {image_path}")

# print the shape - this tells you: (height, width, channels)
print("Shape:", img.shape)

# Print the data type of each pixel value
print("dtype:", img.dtype)

# Print the value pf ONE pixel (row 100, column 100)
# It gives you 3 numbers: Blue, Green, Red (in that order- OpenCV uses BGR, not RGB)
print("Pixel at (100,100):", img[100, 100])

# Show The image in a window
cv2.imshow("My Image", img)

# Wait for any key press, then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()