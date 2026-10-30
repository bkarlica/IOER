import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("img1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("img2.jpg", cv2.IMREAD_GRAYSCALE)
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)
# Apply Lowe's ratio test
good = []
for m, n in matches:
  if m.distance < 0.75 * n.distance:
    good.append([m])
img_matches = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
plt.imshow(img_matches)
plt.title("SIFT Feature Matching")
plt.axis('off')
plt.show()