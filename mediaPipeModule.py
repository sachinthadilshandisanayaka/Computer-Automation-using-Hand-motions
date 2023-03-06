import cv2
import mediapipe as mp
#import pyautogui



class handDetector():
    def __init__(self, mode=False, maxHands=1, detectionCon=0.7, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        #self.screen_width, self.screen_height = pyautogui.size()
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(self.results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
                    #print(handLms)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            #print(myHand)
            h, w, c = img.shape
            
            #index_finger_tip = myHand.landmark[self.mpHands.HandLandmark.INDEX_FINGER_TIP]
            #x, y = int(index_finger_tip.x * self.screen_width), int(index_finger_tip.y * self.screen_height)
            #x1, y2 = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            #print(x, y)
            #print(x1, y2)
            
            for id, lm in enumerate(myHand.landmark):
            
                #h, w, c = img.shape
                #print(w, h)
                #print(lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                #print(x, y)
                #print(cx, cy)
                #if(id == 0):
                 #   print(id, int(lm.z * 100000 * -1))
                #print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList
    
    def findIndexFingePosition(self, img, handNo=0, draw=True):
        lmList = [0, 0, 0]
        if self.results.multi_hand_landmarks:
            
            myHand = self.results.multi_hand_landmarks[handNo]
            #print(myHand)
            h, w, c = img.shape
            
            index_finger_tip = myHand.landmark[self.mpHands.HandLandmark.INDEX_FINGER_TIP]
            #x, y = int(index_finger_tip.x * self.screen_width), int(index_finger_tip.y * self.screen_height)
            cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            lmList = [0, cx, cy]
            #print(x, y)
            #print(x1, y2)

        return lmList


