import pyautogui

def saveImage():
    pyautogui.screenshot('screenshot.png',region=(850,200, 1200, 1200))
