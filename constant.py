import pyautogui

class constants():
    def __init__(self):
        self.screen_cap_frame_devide = 2
        self.screen_scan_frame_devide = 3
        self.screen_width, self.screen_height = pyautogui.size()
        self.capFrameWidth, self.capFrameHeight = int(self.screen_width / self.screen_cap_frame_devide), int(self.screen_height / self.screen_cap_frame_devide)
        self.screen_width_precentage, self.screen_height_precentage = int(self.screen_width / self.screen_scan_frame_devide), int(self.screen_height / self.screen_scan_frame_devide)
        self.top = 10
        self.bottom = int(self.top + self.screen_height_precentage)
        self.right = 300
        self.left = int(self.right + self.screen_width_precentage)
        self.mouseSpeed = 3
        self.middleMinAngle = 13
        self.middleMaxAngle = 150
        self.thumbMinAngle = 75
        self.minDifferenceBetweenTumbAndIndex = 25
        
        
    def getTop(self):
        return self.top
    def getRight(self):
        return self.right
    def getBottom(self):
        return self.bottom
    def getLeft(self):
        return self.left
    def getMoueSpeed(self):
        return self.mouseSpeed
    def getCapFrameWidth(self):
        return self.capFrameWidth
    def getCapFrameHeight(self):
        return self.capFrameHeight
    def getMouseMovingSpeed(self):
        return int(self.screen_scan_frame_devide)
    def getMiddleMinAngle(self):
        return self.middleMinAngle
    def getMiddleMaxAngle(self):
        return self.middleMaxAngle
    def getThumbMinAngle(self):
        return self.thumbMinAngle
    def getDraggingLenght(self):
        return self.minDifferenceBetweenTumbAndIndex

