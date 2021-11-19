import pyperclip
import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]  # 메모장1개
w.activate()

# pyautogui.write("12345")
# pyautogui.write("June's Coding ", interval=0.25)

# 한글처리가 안된다

# pyautogui.write(["t", "e", "s", "t", "left",
#                 "left", "right", "l", "a", "enter"], interval=0.25)


# pyperclip.copy("나도코딩")
# pyautogui.hotkey("ctrl", "v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


my_write("나도코딩")
