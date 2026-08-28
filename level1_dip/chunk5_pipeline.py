import cv2
import numpy as np 
from pathlib import Path

# Setup
# All path relative to tihs script's location 
script_dir = Path(__file__).parent
image_path = script_dir / "test_img.jpg"
output_dir = script_dir / "outputs"

# Create outputs folders if it doesmt exist
output_dir.mkdir(exist_ok=True)

print("=== Level 1 DIP Pipeline ===")
print(f"Input  : {image_path}")
print(f"Output : {output_dir}")

# Step 1 : Load 
img = cv2.imread(str(image_path))
print(f"\nStep 1 - Loaded | Shape: {img.shape}")

# Step 2 : Grayscale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(f"Step 2 - Grayscale | Shape: {gray.shape}")

# Step 3 : SOBEL EDGES 
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel   = cv2.magnitude(sobel_x, sobel_y)
sobel   = np.uint8(np.clip(sobel, 0, 255))
print(f"Step 3 - Sobel edges | Shape: {sobel.shape}")

# Step 4 : Rotation 
height, width = img.shape[:2]
centre = (width // 2, height // 2)
matrix = cv2.getRotationMatrix2D(centre, 45, 1.0)
rotated = cv2.warpAffine(img, matrix, (width, height))
print(f"Step 4 - Roatted 45 degrees | Shape: {rotated.shape}")

# Save all Outputs 
cv2.imwrite(str(output_dir / "1_original.jpg"), img)
cv2.imwrite(str(output_dir / "2_graayscale.jpg"), gray)
cv2.imwrite(str(output_dir / "3_sobel.jpg"), sobel)
cv2.imwrite(str(output_dir / "4_rotated.jpg"), rotated)
print(f"\nAll outputs saved to outputs/ folder")

# Display All 
cv2.imshow("1 - Original", img)
cv2.imshow("2 - Grayscale", gray)
cv2.imshow("3 - Sobel Edges", sobel)
cv2.imshow("4 - rotated 45 degress", rotated)

print("Press any key iside any image window to close.")
cv2.waitKey(0)
cv2.destroyAllWindows()
print("\nDone.")