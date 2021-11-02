import pyautogui
from pyscreeze import pixelMatchesColor

pyautogui.sleep(3)

img = pyautogui.screenshot()
img.save("screenshot.png")


# pyautogui.mouseInfo()


pixel = pyautogui.pixel(28, 18)

print(pixel)
