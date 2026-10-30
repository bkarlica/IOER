import cv2
import numpy as np
# Load image from disk
image_path = 'PST_1920x1088_cam4.png'
img = cv2.imread(image_path)
# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Optional: Apply Gaussian Blur to reduce noise
blurred_img = cv2.GaussianBlur(gray_img, (3, 3), 0)
cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Suppose we have a grayscale image in 'gray_img'
sobel_x = cv2.Sobel(blurred_img, cv2.CV_64F, 1, 0, ksize=5) # x derivative
sobel_y = cv2.Sobel(blurred_img, cv2.CV_64F, 0, 1, ksize=5) # y derivative

# Convert to absolute values and 8-bit
abs_sobel_x = cv2.convertScaleAbs(sobel_x)
abs_sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine the two directions
sobel_combined = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

_, thresh_20 = cv2.threshold(sobel_combined, 20, 255, cv2.THRESH_BINARY)
_, thresh_50 = cv2.threshold(sobel_combined, 50, 255, cv2.THRESH_BINARY)
_, thresh_100 = cv2.threshold(sobel_combined, 100, 255, cv2.THRESH_BINARY)

# Show everything together
cv2.imshow('Sobel X', abs_sobel_x)
cv2.imshow('Sobel Y', abs_sobel_y)
cv2.imshow('Sobel Combined', sobel_combined)
cv2.imshow('Threshold 20', thresh_20)
cv2.imshow('Threshold 50', thresh_50)
cv2.imshow('Threshold 100', thresh_100)

cv2.waitKey(0)
cv2.destroyAllWindows()

scharr_x = cv2.Scharr(blurred_img, cv2.CV_64F, 1, 0)
scharr_y = cv2.Scharr(blurred_img, cv2.CV_64F, 0, 1)

abs_scharr_x = cv2.convertScaleAbs(scharr_x)
abs_scharr_y = cv2.convertScaleAbs(scharr_y)

scharr_combined = cv2.addWeighted(abs_scharr_x, 0.5, abs_scharr_y, 0.5, 0)

cv2.imshow('Scharr X', abs_scharr_x)
cv2.imshow('Scharr Y', abs_scharr_y)
cv2.imshow('Scharr Combined', scharr_combined)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Define Prewitt kernels
kernel_prewitt_x = np.array([[-1, 0, 1],
                            [-1, 0, 1],
                            [-1, 0, 1]], dtype=np.float32)

kernel_prewitt_y = np.array([[-1, -1, -1],
                            [ 0, 0, 0],
                            [ 1, 1, 1]], dtype=np.float32)

prewitt_x = cv2.filter2D(blurred_img, -1, kernel_prewitt_x)
prewitt_y = cv2.filter2D(blurred_img, -1, kernel_prewitt_y)

prewitt_combined = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)

cv2.imshow('Prewitt X', prewitt_x)
cv2.imshow('Prewitt Y', prewitt_y)
cv2.imshow('Prewitt Combined', prewitt_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()