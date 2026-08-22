import cv2
from pathlib import Path

# Load the image (same as before)
image_path = Path(__file__).with_name("test_img.jpg")
img = cv2.imread(str(image_path))

# Convert colour image to grayscale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Check the shape - notice something cahnged
print("Colour iage shape:", img.shape)
print("Grayscale image shape:", gray.shape)

#Check on the pixel value 
print("Colour pixel at (100,100):", img[100,100])
print("Grayscale pixel at (100,100):", gray[100,100])

#Show the both images side by side 
cv2.imshow("Orginal", img)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllwindow()