import cv2 as cv
import numpy as np

BACKGROUND_MODEL = 'median'
#BACKGROUND_MODEL = 'mean'

cap = cv.VideoCapture('highway.mp4')

frames = []
for fid in range(101):
    cap.set(cv.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    if ret:
        frames.append(frame)

if BACKGROUND_MODEL == 'median':
    background = np.median(frames, axis=0).astype(np.uint8)
    print("Using MEDIAN background model")
else:
    background = np.mean(frames, axis=0).astype(np.uint8)
    print("Using MEAN background model")

bg_gray = cv.cvtColor(background, cv.COLOR_BGR2GRAY)  #background to grayscale

cap.set(cv.CAP_PROP_POS_FRAMES, 0)  #rewind video to start

cv.namedWindow('Frame', cv.WINDOW_NORMAL)
cv.namedWindow('FG Mask', cv.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()

    if ret is True:
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)   # current frame to grayscale

        difference = cv.absdiff(frame_gray, bg_gray)  #subtracting background from current 

        _, fgMask = cv.threshold(difference, 25, 255, cv.THRESH_BINARY)

        cv.imshow('Frame', frame)
        cv.imshow('FG Mask', fgMask)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv.destroyAllWindows()