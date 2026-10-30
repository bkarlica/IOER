import numpy as np
import cv2

# Open Video

cap = cv2.VideoCapture('highway.mp4')

number_of_frame=0
frameIds = []



while number_of_frame < 101:
    frameIds.append(number_of_frame)   
    number_of_frame=number_of_frame+1


# Store selected frames in an array
frames = []

for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)

# Calculate the mean along the time axis
meanFrame = np.mean(frames, axis=0).astype(dtype=np.uint8)   

# Calculate the median along the time axis
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)  

 

# Display median frame
cv2.imshow('median frame', medianFrame)
cv2.imwrite('medianFrame.jpg', medianFrame, [cv2.IMWRITE_JPEG_QUALITY, 100])

# Display mean frame
cv2.imshow('mean frame', meanFrame)
cv2.imwrite('meanFrame.jpg', meanFrame, [cv2.IMWRITE_JPEG_QUALITY, 100])



    
cv2.waitKey(0)

# When everything is done, release the video capture object

cap.release()
# Closes all frames
cv2.destroyAllWindows() 
