import cv2
import numpy as np

# Start video capture
cap = cv2.VideoCapture(0)

# Initial parameters
ksize = 3          # Sobel kernel size (must be 1,3,5,7)
blur_level = 3     # Gaussian blur kernel size (odd number)
threshold_val = 100  # Threshold for edge binary

def nothing(x):
    pass

# Create window with trackbars to adjust parameters in real time
cv2.namedWindow('Camera - Sobel Edges')
cv2.createTrackbar('Blur', 'Camera - Sobel Edges', blur_level, 15, nothing)
cv2.createTrackbar('Sobel ksize', 'Camera - Sobel Edges', ksize, 7, nothing)
cv2.createTrackbar('Threshold', 'Camera - Sobel Edges', threshold_val, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Get current values from trackbars
    blur_level = cv2.getTrackbarPos('Blur', 'Camera - Sobel Edges')
    ksize = cv2.getTrackbarPos('Sobel ksize', 'Camera - Sobel Edges')
    threshold_val = cv2.getTrackbarPos('Threshold', 'Camera - Sobel Edges')

    # Ensure odd kernel sizes for Gaussian and Sobel
    if blur_level % 2 == 0:
        blur_level += 1
    if ksize % 2 == 0:
        ksize += 1
    if ksize == 0:
        ksize = 1

    # Preprocessing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (blur_level, blur_level), 0)

    # Sobel edge detection
    sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=ksize)
    sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=ksize)
    abs_sobel_x = cv2.convertScaleAbs(sobel_x)
    abs_sobel_y = cv2.convertScaleAbs(sobel_y)
    sobel_combined = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

    # Apply threshold
    _, sobel_thresh = cv2.threshold(sobel_combined, threshold_val, 255, cv2.THRESH_BINARY)

    # Show both raw Sobel and thresholded
    cv2.imshow('Camera - Sobel Edges', sobel_combined)
    cv2.imshow('Camera - Sobel Threshold', sobel_thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

