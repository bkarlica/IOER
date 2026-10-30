import cv2
import numpy as np


currentFrame = cv2.imread('currentFrame.jpg',cv2.IMREAD_UNCHANGED)
backgroundModel = cv2.imread('medianFrame.jpg',cv2.IMREAD_UNCHANGED)


first_gray = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY)
gray_frame = cv2.cvtColor(backgroundModel, cv2.COLOR_BGR2GRAY)
        
difference = cv2.absdiff(first_gray, gray_frame)
_, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

cv2.imshow("Current frame", currentFrame)
cv2.imshow("Background Model", backgroundModel)
cv2.imshow("thresholded difference", difference)

cv2.waitKey(0)
cv2.destroyAllWindows()
