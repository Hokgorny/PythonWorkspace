import time
import pyautogui
import pywinauto
import pygetwindow

curr_win = pyautogui.getActiveWindow() # 현재 활성화된 창
print(curr_win.left, curr_win.top, curr_win.right, curr_win.bottom)
print(curr_win.size)