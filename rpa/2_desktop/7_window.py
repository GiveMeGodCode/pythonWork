import pyautogui

# fw = pyautogui.getActiveWindow()  # 활성화된 창 정보 (vscode)
# print(fw.title)  # 창제목
# print(fw.size)  # 창크기
# print(fw.left, fw.top, fw.right, fw.bottom)

# pyautogui.moveTo(fw.left + 20, fw.top+20)

# for w in pyautogui.getAllWindows():
#     print(w)


# for w in pyautogui.getWindowsWithTitle("제목 없음"):
#     print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)

if w.isActive == False:
    w.activate()

pyautogui.sleep(1)

if w.isMaximized == False:
    w.maximize()  # 최대화

pyautogui.sleep(1)

w.restore()
pyautogui.sleep(1)

w.close()
# if w.isMinimized == False:
#     w.minimize()
