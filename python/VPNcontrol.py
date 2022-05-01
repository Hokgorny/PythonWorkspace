import time
import pyautogui
import pywinauto
import pygetwindow


def find_target(img_file, timeout=10):
    start = time.time()
    target = None
    while target is None:
        curr_win = pyautogui.getActiveWindow() # 범위 지정을 위해 현재 활성화된 창 이용
        target = pyautogui.locateOnScreen(img_file, grayscale=True, region=(curr_win.left, curr_win.top, curr_win.width, curr_win.height))
        end = time.time()
        if end - start > timeout:
            break
    return target

def img_click(img_file, timeout=10, clicknum=1):
    target = find_target(img_file, timeout=30)
    if target:
        pyautogui.click(target, clicks=clicknum)
    else:
        print(f"[{timeout}초 경과] 타겟 미발견 {img_file}.")


# SoftEtherVPN 창이 비활성화된 경우 활성화
SoftEther = pygetwindow.getWindowsWithTitle('SoftEther VPN Client Manager')[0]
if SoftEther.isActive == False:
    pywinauto.application.Application().connect(handle=SoftEther._hWnd).top_window().set_focus()
SoftEther.activate()

# VPN 변경
img_click("1.png", "", 2)   # VPN Gate Public VPN Relay Servers 버튼 클릭
img_click("2.png",)         # Region 버튼 클릭 <- 시간소요 줄일 필요 있음
# pyautogui.scroll(-300)    # 스크롤내리기
pyautogui.press("Down")     # 다음 VPN 선택, 엔터키로 클릭
pyautogui.press("Enter")    # 
pyautogui.press("Enter")

# button_ok = pyautogui.locateOnScreen("4.png")       # OK 버튼 나올 때 까지 대기
# while button_ok is None:                            #
#     button_ok = pyautogui.locateOnScreen("4.png")   #
# pyautogui.click("4.png")
# button_close = pyautogui.locateOnScreen("5.png")       # Close 버튼 나올 때 까지 대기
# while button_close is None:                            #
#     button_close = pyautogui.locateOnScreen("5.png")   #
# pyautogui.press("Enter")    # 완료 창 닫기, VPN 변경 완료
