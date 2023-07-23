import cv2
import imutils
import mediaPipeModule as htm
import pyautogui
import constant as const
import curserController as cc

const = const.constants()
font = cv2.FONT_HERSHEY_SIMPLEX

maximemangle = [60, 15, 13, 20]

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

detector = htm.handDetector(detectionCon=1)
cController = cc.curserController(False);

# Set up the PyAutoGUI mouse control parameters
screen_width, screen_height = pyautogui.size()
mouse_speed = const.getMoueSpeed()

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read()
    
    #change camera view resolution
    img = imutils.resize(img, width=const.getCapFrameWidth(), height=const.getCapFrameWidth())
    
    # flipping the image horizontally (around the y-axis) 
    img = cv2.flip(img,1)
    img = cv2.rectangle(img, (const.getLeft(), const.getTop()), (const.getRight(), const.getBottom()), (0,255,0), 2)
    roi = img[const.getTop():const.getBottom(), const.getRight():const.getLeft()]
    
    roi = detector.findHands(roi)
    
    lmList = detector.findPosition(roi, draw=False)
    LM_INDEX_FINGER = detector.findIndexFingePosition(roi, draw=False)
    #print(LM_INDEX_FINGER)
    
    #cv2.imshow("Image", img)
    if len(lmList) != 0:
        if len(lmList) == 21:
            # move curser
            cController.moveCurser(LM_INDEX_FINGER, lmList, img)
        else:
            cv2.putText(img,'Full Hand not visible',(0,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
    
    cv2.imshow("Camera View", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #print(range(defects.shape[0]))
        break

cap.release()
cv2.destroyAllWindows()





