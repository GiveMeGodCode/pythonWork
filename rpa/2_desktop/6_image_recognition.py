from PIL.ImageOps import grayscale
import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)


# alarm_icon = pyautogui.locateOnScreen("alarm.png")
# pyautogui.moveTo(alarm_icon)


# for i in pyautogui.locateAllOnScreen("check_box.png"):
#     print(i)
#     pyautogui.click(i)


# check_box = pyautogui.locateOnScreen("alarm.png")
# pyautogui.click(check_box)


# GrayScale.

check_box = pyautogui.locateOnScreen("alarm.png", grayscale=True)
pyautogui.click(check_box)
