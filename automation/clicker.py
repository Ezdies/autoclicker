import pyautogui

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
