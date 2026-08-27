import cv2
import numpy as np 
from pathlib import Path 

# Load Image 
image_path = Path(__file__).with_name("test_img.jpg")
img = cv2.imread(str(image_path))

# Get the centre of the image 
# img.shape gives (height, width, channels)
height = img.shape[0]
width = img.shape[1]
centre = (width // 2, height // 2)

print("Image size", width, "x", height)
print("Centre Point:", centre)

# Build the roattion matrix 
# Arguments: centre point, angle in degrees , scale (1.0 = no zoom)
angle = 45
matrix = cv2.getRotationMatrix2D(centre, angle, 1.0)

print("Rotation matrix shape :", matrix.shape)
print("Rotation matrix:")
print(matrix)

# Apply the roattion to the image 
rotated = cv2.warpAffine(img, matrix, (width, height))

# Show orginal and rotated 
cv2.imshow("Original", img)
cv2.imshow("Rotated 45 degrees", rotated)
cv2.waitKey(0)
cv2.destrpyAllWindows()
