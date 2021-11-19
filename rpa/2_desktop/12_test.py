import pyautogui
import sys
import pyperclip

pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")

pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]

window.maximize()

# 글자클릭
btn_text = pyautogui.locateOnScreen("btn_text.png", confidence=0.8)

if btn_text:
    pyautogui.click(btn_text)
else:
    sys.exit()

pyautogui.moveTo(200, 200, duration=0.5)
pyautogui.click()
pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl", "v")

window.close()
