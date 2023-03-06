import pyautogui
import constant as const
import math
import angleCalculator
import cv2

const = const.constants()
font = cv2.FONT_HERSHEY_SIMPLEX

class curserController():
    
    def __init__(self, isMiddleFingerUp_ = False, isMouseLeftClick = False):
        self.isMouseLeftClick =  isMouseLeftClick;
        self.isMiddleFingerUp_ = isMiddleFingerUp_
        self.screen_width, self.screen_height = pyautogui.size()
        self.mouse_speed = const.getMoueSpeed()
        self.isMiddleFingerUpCounter = 0;
        
    def clickMouse(self):
        return pyautogui.click()
        
    def moveCurser(self, indexFinger = [0, 0, 0], lmList = [], img = None):
        self.lmList = lmList
        self.angleCalculater = angleCalculator.angleCalculator(lmList)
        indexFingerHeight = math.sqrt((self.lmList[5][1] - self.lmList[8][1])**2 + (self.lmList[5][2] - self.lmList[8][2])**2)
        middleFingerHeight = math.sqrt((self.lmList[9][1] - self.lmList[12][1])**2 + (self.lmList[9][2] - self.lmList[12][2])**2)
        #print(indexFingerHeight)
        #print(middleFingerHeight)
        
        
        angle = self.angleCalculater.calculateAngleWristAndMidddle()
        #print("angle", angle)
        if (angle > const.getMiddleMinAngle() and angle < const.getMiddleMaxAngle()):
            
            isMiddleFingerUp = self.angleCalculater.isMiddleFingerUp()
           
            if (isMiddleFingerUp):
                if img is not None:
                    cv2.putText(img,'Double',(0,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
                    
                if (self.isMiddleFingerUp_ is False):
                    self.isMiddleFingerUp_ = True
                    pyautogui.doubleClick()
    
            else:
                self.isMiddleFingerUp_ = False
                
                x, y = indexFinger[1] , indexFinger[2]
                if (x > 0 and y > 0):
                    current_x, current_y = pyautogui.position()
                    new_x = current_x + ((x * const.getMouseMovingSpeed()) - current_x) / self.mouse_speed
                    new_y = current_y + ((y * const.getMouseMovingSpeed()) - current_y) / self.mouse_speed
                    
                    # angle between Thumb and index finger
                    if (const.getThumbMinAngle() <= self.angleCalculater.calculateAngleThumAndIndex()):
                        if img is not None:
                            cv2.putText(img,'Mouse click down',(0,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
                        if (self.isMouseLeftClick is False):
                            pyautogui.mouseDown()
                        pyautogui.moveTo(new_x, new_y)
                        self.isMouseLeftClick = True
                        
                    else:
                        if (self.isMouseLeftClick is True):
                            cv2.putText(img,'Mouse click up',(0,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
                            pyautogui.mouseUp()
                            self.isMouseLeftClick = False
                            
                        # mouse draging
                        isDragging = self.angleCalculater.isDragging()
                        if (isDragging is True):
                            cv2.putText(img,'Draggging',(0,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
                            pyautogui.dragTo(new_x, new_y)
                        else:
                            if img is not None:
                                cv2.putText(img,'Moving',(0,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
                        
                            if (new_x >= self.screen_width):
                                return pyautogui.moveTo(int(self.screen_width -6), new_y)
                            else:
                                if (new_y >= self.screen_height):
                                    return pyautogui.moveTo(new_x, int(self.screen_height - 6))
                                else:
                                    return pyautogui.moveTo(new_x, new_y)
        else:
            print('Angle incorrect')
            
            
            
            
            