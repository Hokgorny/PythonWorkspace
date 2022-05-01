# 디시 개추 주작기

# 1. 게시글 주소 입력
# 2. 필요한 엘리먼트 가져오기(+자동입력방지문자 존재 유무 확인)
# 3. 아이피 바꾸기 (proxy rotating)
# 4 - 1. 자동입력방지문자 존재시, ocr사용 후 입력(부재시 바로 4 - 2)

import requests
import threading

from faulthandler import is_enabled
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def jujak():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    #options.add_argument('--proxy-server=socks5://127.0.0.1:9150') # tor proxy 사용
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25")
    # options.add_argument("--start-maximized")


    driver = webdriver.Chrome("./chromedriver.exe" , options=options)
    driver.maximize_window()
    driver.get('https://gall.dcinside.com/board/view/?id=baseball_new10&no=12727004&page=1')

    # try:
    #     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/section/article[2]/div[1]/div/div[3]/div[1]/button")))
    # except Exception as e:
    #     print("error :", e)

    gaechu = driver.find_element_by_xpath("//*[@id='container']/section/article[2]/div[1]/div/div[3]/div[1]/button")
    print(gaechu.is_enabled())     
    gaechu.click()
    input()
    # gaechu.send_keys(Keys.ENTER)
    # driver.execute_script("arguments[0].click();", gaechu)
jujak()

# 쓰레드 생성 및 실행
# threads = []

# for i in range(5):
#     t = threading.Thread(target=jujak)
#     threads.append(t)

# for t in threads:
#     t.start()
