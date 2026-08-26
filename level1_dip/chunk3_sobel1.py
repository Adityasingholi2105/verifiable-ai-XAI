import cv2
import numpy as np 
from pathlib import Path

# Load and converet to grayscale first 
# Sobel works on single-channel images 
image_path = Path(__file__).with_name("test_img.jpg")
img = cv2.imread(str(image_path))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel in X direction - Detects Certical edges 
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Sobel in Y direction - detects horizontal edges 
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Combine both directions to get all edges 
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Convert back to uint8 (0-255) for display 
sobel_display = np.uint8(np.clip(sobel_combined, 0, 255))

#Print shapes to confirm nothing changed
print("Gray Shape:", gray.shape)
print("Sobel X shape:", sobel_x.shape)
print("Sobel combined shape:", sobel_combined.shape)

# Show all three 
cv2.imshow("Grayscale", gray)
cv2.imshow("Sobel X (vertical edges)", np.uint8(np.clip(np.abs(sobel_x), 0, 255)))
cv2.imshow("Sobel Combined (all edges)", sobel_display)
cv2.waitKey(0)
cv2.destroyAllWindows()
