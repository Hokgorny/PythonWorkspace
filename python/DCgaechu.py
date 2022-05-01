# 디시 개추 주작기

# 1. VPN으로 IP 바꾸기
# 2. Selenium으로 디시 접속 후 개추 엘리먼트 가져오기
# 3. 자동입력방지문자 존재유무 확인
# 3 - 1. 부재시 바로 개추 클릭
# 3 - 2. 존재시 ocr처리 후 개추 클릭 <- 미구현

import time, pyautogui, pywinauto, pygetwindow
from faulthandler import is_enabled
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# def find_target(img_file, timeout=10):
#     start = time.time()
#     target = None
#     while target is None:
#         curr_win = pyautogui.getActiveWindow() # 범위 지정을 위해 현재 활성화된 창 이용
#         target = pyautogui.locateOnScreen(img_file, grayscale=True, region=(curr_win.left, curr_win.top, curr_win.width, curr_win.height))
#         end = time.time()
#         if end - start > timeout:
#             break
#     return target

# def img_click(img_file, timeout=10, clicknum=1):
#     target = find_target(img_file, timeout=30)
#     if target:
#         pyautogui.click(target, clicks=clicknum)
#     else:
#         print(f"[{timeout}초 경과] 타겟 미발견 {img_file}.")

# # # 1. VPN으로 IP 바꾸기
# # SoftEtherVPN 창이 비활성화된 경우 활성화
# SoftEther = pygetwindow.getWindowsWithTitle('SoftEther VPN Client Manager')[0]
# if SoftEther.isActive == False:
#     pywinauto.application.Application().connect(handle=SoftEther._hWnd).top_window().set_focus()
# SoftEther.activate()

# # VPN 변경
# img_click("1.png", "", 2)   # VPN Gate Public VPN Relay Servers 버튼 클릭
# img_click("2.png",)         # Region 버튼 클릭 <- 시간소요 줄일 필요 있음
# pyautogui.press("Down")     # 다음 VPN 선택, 엔터키로 클릭
# pyautogui.press("Enter")    # 
# pyautogui.press("Enter")    #

# # 2. Selenium으로 디시 접속 후 개추 엘리먼트 가져오기 + 클릭
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument('headless')

driver = webdriver.Chrome("./chromedriver.exe" , options=options)
driver.maximize_window()
driver.get('https://gall.dcinside.com/mgallery/board/view/?id=iptime&no=2&page=1')

# try:
#     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/section/article[2]/div[1]/div/div[3]/div[1]/button")))
# except Exception as e:
#     print("error :", e)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='container']/section/article[2]/div[1]/div/div[3]/div[1]/button")))
driver.find_element_by_xpath("//*[@id='container']/section/article[2]/div[1]/div/div[3]/div[1]/button").click()

input()