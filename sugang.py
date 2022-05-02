# 부산대학교 수강신청 툴
# 1. 수강신청 로그인 페이지 진입
# 2. 수강신청 페이지 진입할 때까지 로그인 버튼 반복 클릭 
# 3. 수강신청 페이지 진입 후, 희망과목 수강신청 버튼 클릭

import sys, time, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from twilio.rest import Client

# 0. 기본 설정(twilio API, 상태 체크)
client = Client("", "")
curr_status = True
def check_status(): # 현 상태 체크, 오류 발생시 프로그램 종료
    if curr_status == False:
        time.sleep(5)
        sys.exit()

# 1. 수강신청 로그인 페이지 진입
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://sugang.pusan.ac.kr/sugang/Login.aspx")

# 2. 수강신청 페이지 진입할 때까지 로그인 엘리먼트 반복 클릭
print("\n로그인 정보 입력... 정확히 입력해 주세요.")
id = input("학번 입력 : ")
pw = input("비밀번호 입력 : ")
print("입력 완료! 잠시후 7시 55분 55초부터 로그인을 시도합니다.\n")

try:
    client.messages.create(to ="", from_ = "", body = f"학번 {id} : 프로그램 사용")
except:
    pass

curr_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).time()
ob_time = datetime.time(7, 55, 55)
while curr_time <= ob_time:
    curr_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).time()
    time.sleep(0.01)
    print(f"현재시간(UTC) : {curr_time}", end="\r")
print("\n\n로그인 시작")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtid']")))
driver.find_element(by=By.XPATH, value="//*[@id='txtid']").send_keys(id)

num_of_attempts = 1
while driver.current_url != "https://sugang.pusan.ac.kr/sugang/Sugang-insert.aspx":
    try: # 하얀화면에서 url이 업데이트 되지 않을 경우 대비 예외처리(아마 일어나지 않을 것임)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtpassword']")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='btnlogin']")))
        driver.find_element(by=By.XPATH, value="//*[@id='txtpassword']").send_keys(pw)
        driver.find_element(by=By.XPATH, value="//*[@id='btnlogin']").click()
        print(f"로그인 {num_of_attempts}회 시도")
        num_of_attempts += 1
    except:
        pass
print("로그인 성공!\n")

# 3. 수강신청 페이지 진입 후, 희망과목 수강신청 엘리먼트 클릭
try:
    WebDriverWait(driver, 90).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@id,'_bt신청')]")))
except TimeoutException:    # 희망담기한 과목이 없을 경우
    print("희망과목담기에 과목이 없습니다. 프로그램을 종료합니다.")
    curr_status = False
check_status()

subjects = driver.find_elements(by=By.XPATH, value="//*[contains(@id,'_bt신청')]")
for i in range (0, len(subjects)):
    subjects[i].click()
    WebDriverWait(driver, 90).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@id,'_bt신청')]")))
    subjects = driver.find_elements(by=By.XPATH, value="//*[contains(@id,'_bt신청')]")
    try: # 수강신청 당일 결과창이 늦게 뜨는 경우 대비 예외처리
        res = driver.find_element(by=By.XPATH, value="//*[@id='lbError']")
        print(f"{i+1}번째 과목 : {res.text}\n")
    except:
        print(f"{i+1}번째 과목 : 신청 성공!(서버렉으로 인해 자세한 정보가 표기되지 않음)\n")
print("수강신청 완료! 프로그램을 닫아도 좋습니다.")