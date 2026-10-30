
import cv2 as cv



# MOG2
#backSub = cv.createBackgroundSubtractorMOG2()
#backSub = cv.createBackgroundSubtractorMOG2(history=120, varThreshold=50, detectShadows=True)
#backSub = cv.createBackgroundSubtractorMOG2(history=50, varThreshold=25, detectShadows=False)

# KNN
backSub = cv.createBackgroundSubtractorKNN()


cap = cv.VideoCapture('highway.mp4')
if not cap.isOpened:
    print('Unable to open file')
    exit(0)

cv.namedWindow('Frame', cv.WINDOW_NORMAL)
cv.namedWindow('FG Mask', cv.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    
    
    
    if ret is True:
        
    
        fgMask = backSub.apply(frame)
    
    
    
    
        cv.imshow('Frame', frame)
        cv.imshow('FG Mask', fgMask)
    
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
            
            
    else:
        break
        
        
        
cap.release()
# Closes all frames
cv.destroyAllWindows() 