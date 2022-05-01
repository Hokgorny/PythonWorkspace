# import pywinauto
# from pywinauto.application import Application

# SoftEther = Application(backend="uia").connect(process=28444)
# dlg = SoftEther["SoftEther VPN Client Manager"]
# dlg2 = dlg.child_window(auto_id="1047", control_type="List")
# dlg3 = dlg2.child_window(title="VPN Gate Public VPN Relay Servers", control_type="ListItem")
# dlg4 = dlg3.child_window(title="VPN Gate Public VPN Relay Servers", control_type="Edit")
# dlg3.type_keys("{Enter}")
# # dlg3.child_window(title="VPN Gate Public VPN Relay Servers", control_type="Edit").select()

import time, pyautogui, pywinauto, pygetwindow
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://gall.dcinside.com/mgallery/board/view/?id=bubblefighter&no=24434&page=9")
driver.maximize_window()
for i in range(1,100):
    # SoftEtherVPN 창이 비활성화된 경우 활성화
    SoftEther = pygetwindow.getWindowsWithTitle("SoftEther VPN Client Manager")[0]
    
    if SoftEther.isActive == False:
        pywinauto.application.Application().connect(handle=SoftEther._hWnd).top_window().set_focus()
    SoftEther.activate()
    # VPN 변경 매크로
    pyautogui.press("Enter")
    time.sleep(0.3)
    curr_win = pyautogui.getActiveWindow()
    pyautogui.click(curr_win.left+450, curr_win.top+200)
    pyautogui.press("Enter")
    time.sleep(0.3)
    pyautogui.press("Down")
    pyautogui.press("Enter")
    time.sleep(0.3)
    pyautogui.press("Enter")
    # 개추 클릭
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='container']/section/article[2]/div[1]/div/div[3]/div[1]/button")))
    except UnexpectedAlertPresentException:
        pyautogui.press("Enter")
    driver.find_element_by_xpath("//*[@id='container']/section/article[2]/div[1]/div/div[3]/div[1]/button").click()
    driver.delete_all_cookies
input()