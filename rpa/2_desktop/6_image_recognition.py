import sys
import time
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
# check_box = pyautogui.locateOnScreen("alarm.png", grayscale=True, region)
# check_box = pyautogui.locateOnScreen(
#     "trash_icon.png", region=(1488, 623, 1881-1488, 137))
# pyautogui.moveTo(check_box)


# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.7)
# pyautogui.moveTo(run_btn)


# 바로 안보일때
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견실패")

# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견실패")


# timeout = 10
# start = time.time()
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen(
#         "file_menu_notepad.png", confidence=0.7)
#     end = time.time()  # 종료시간
#     if end-start > timeout:
#         print("시간초과")
#         sys.exit()


# pyautogui.click(file_menu_notepad)


def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file, confidence=0.8)
        end = time.time()
        if end - start > timeout:
            break
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(
            f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()


my_click("file_menu_notepad.png")
