import pyautogui
import math
import constant as const

const = const.constants()
class angleCalculator():
    def __init__(self, lmList):
        self.screen_width, self.screen_height = pyautogui.size()
        self.lmList = lmList
        
    def calculateAngleWristAndMidddle(self):
        # Assume MIDDLE_FINGER_TIP and WRIST are tuples representing the (x, y, z) coordinates of the landmarks
        MIDDLE_FINGER_TIP = (self.lmList[12][1], self.lmList[12][2], 0)
        WRIST = (self.lmList[0][1], self.lmList[0][2], 0)

        # Calculate the vectors between MIDDLE_FINGER_TIP and WRIST, and between MIDDLE_FINGER_TIP and the x-axis
        vec1 = (WRIST[0] - MIDDLE_FINGER_TIP[0], WRIST[1] - MIDDLE_FINGER_TIP[1], WRIST[2] - MIDDLE_FINGER_TIP[2])
        vec2 = (1, 0, 0)

        # Calculate the dot product and the cross product of the two vectors
        dot_product = vec1[0] * vec2[0] + vec1[1] * vec2[1] + vec1[2] * vec2[2]
        cross_product = (vec1[1] * vec2[2] - vec1[2] * vec2[1], vec1[2] * vec2[0] - vec1[0] * vec2[2], vec1[0] * vec2[1] - vec1[1] * vec2[0])

        # Calculate the angle between the two vectors
        angle = math.atan2(math.sqrt(cross_product[0] ** 2 + cross_product[1] ** 2 + cross_product[2] ** 2), dot_product) * 180 / math.pi
        return angle
    
    def calculateAngleThumAndIndex(self):
        a = math.sqrt((self.lmList[4][1] - self.lmList[8][1])**2 + (self.lmList[4][2] - self.lmList[8][2])**2)
        b = math.sqrt((self.lmList[0][1] - self.lmList[8][1])**2 + (self.lmList[0][2] - self.lmList[8][2])**2)
        c = math.sqrt((self.lmList[4][1] - self.lmList[0][1])**2 + (self.lmList[4][2] - self.lmList[0][2])**2)
        #s = (a+b+c)/2
        #ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
        #d =(2*ar)/a
        
        # apply cosine rule here
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 100
        return angle
    
    def isMiddleFingerUp(self):
        MIDDLE_FINGER_TIP = (self.lmList[12][1], self.lmList[12][2], 0)
        MIDDLE_FINGER_DIP = (self.lmList[11][1], self.lmList[11][2], 0)
        #print('MIDDLE_FINGER_TIP', MIDDLE_FINGER_TIP[1])
        #print('MIDDLE_FINGER_DIP', MIDDLE_FINGER_DIP[1])
        return MIDDLE_FINGER_TIP[1] < MIDDLE_FINGER_DIP[1]
    
    def isDragging(self):
        THUMB_TIP = (self.lmList[4][1], self.lmList[4][2], 0)
        INDEX_FINGER_TIP = (self.lmList[8][1], self.lmList[8][2], 0)
        dfX = abs(THUMB_TIP[0] - INDEX_FINGER_TIP[0])
        dfY = abs(THUMB_TIP[1] - INDEX_FINGER_TIP[1])
        if (dfX < const.getDraggingLenght() and dfY < const.getDraggingLenght()):
            return True
        else:
            return False
        
        