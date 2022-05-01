# 부산대학교 수강신청 툴
# 1. 수강신청 로그인 페이지 진입
# 2. 수강신청 페이지 진입할 때까지 로그인 버튼 반복 클릭 
# 3. 수강신청 페이지 진입 후, 희망과목 수강신청 버튼 클릭

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

curr_status = True
def check_status(): # 현 상태 체크, 오류 발생시 프로그램 종료
    if curr_status == False:
        time.sleep(5)
        sys.exit()

# 1. 수강신청 로그인 페이지 진입
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://sugang.pusan.ac.kr/sugang/Login.aspx")

# 2. 수강신청 페이지 진입할 때까지 로그인 버튼 반복 클릭
print("\n로그인 정보 입력... 정확히 입력해 주세요.")
id = input("학번 입력 : ")
pw = input("비밀번호 입력 : ")
print("\n로그인 시작")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtid']")))
driver.find_element(by=By.XPATH, value="//*[@id='txtid']").send_keys(id)

num_of_attempts = 1
while driver.current_url != "https://sugang.pusan.ac.kr/sugang/Sugang-insert.aspx":
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtid']")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtpassword']")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='btnlogin']")))
    driver.find_element(by=By.XPATH, value="//*[@id='txtpassword']").send_keys(pw)
    driver.find_element(by=By.XPATH, value="//*[@id='btnlogin']").click()
    print(f"로그인 {num_of_attempts}회 시도")
    num_of_attempts += 1
print("로그인 성공\n")