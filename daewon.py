import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display
from twilio.rest import Client

# ubuntu 서버에서 실행시키기 위해 가상 디스플레이 설정
display = Display(visible=0, size=(1920, 1080))
display.start()

# 기본 정보
id = [""]
pw = [""]
points = list(0 for _ in range(0, len(id)))
account_sid = ""
auth_token = ""

def send_msg(): # 문자 전송 함수
    client = Client(account_sid, auth_token)
    client.messages.create(to ="", from_ = "", body = f"\n출석체크 완료(적립금은 아래)\n{id[0]} : {points[0]}P\n{id[1]} : {points[1]}P\n{id[2]} : {points[2]}P")

def get_new_driver(): # driver 생성 함수
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.daewonshop.com/mypage/mileage.php")

    return driver

def dw_login(driver, id, pw): # 대원샵 출석체크 및 누적 적립금 추출 함수
    driver.get("https://www.daewonshop.com/mypage/mileage.php")
    # id, pw 입력 후 로그인 버튼 클릭
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginId']")))
    driver.find_element(By.XPATH, value="//*[@id='loginId']").clear()
    driver.find_element(By.XPATH, value="//*[@id='loginId']").send_keys(id)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginPwd']")))
    driver.find_element(By.XPATH, value="//*[@id='loginPwd']").send_keys(pw)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='formLogin']/div[1]/button/em")))
    driver.find_element(By.XPATH, value="//*[@id='formLogin']/div[1]/button/em").click()

    try: # 알림창 제어
        time.sleep(3)
        da = Alert(driver)
        da.accept()
    except:
        pass

    # 적립금 추출 및 저장
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/table/tbody/tr/th/span[2]")))
    point = driver.find_element(By.XPATH, value="//*[@id='content']/div/table/tbody/tr/th/span[2]")
    points[i] = point.text

    # 로그아웃
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='top']/div[2]/div/ul/li[1]/a")))
    driver.find_element(By.XPATH, value="//*[@id='top']/div[2]/div/ul/li[1]/a").click()

    try: # 알림창 제어
        time.sleep(3)
        da2 = Alert(driver)
        da2.accept()
    except:
        pass

if __name__ == "__main__":
    driver = get_new_driver()
    for i in range(0, len(id)):
        dw_login(driver, id[i], pw[i])

    print(points)
    send_msg()