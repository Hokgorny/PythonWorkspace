import time, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import pyperclip, keyboard

idy = ""
pwy = ""
idn = ""
pwn = ""

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# 네이버 로그인
driver.get("https://www.naver.com/")
driver.find_element(By.XPATH, value="//*[@id='account']/a").click()
pyperclip.copy(idn)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='id']")))
driver.find_element(By.XPATH, value="//*[@id='id']").send_keys(Keys.CONTROL + 'v')
pyperclip.copy(pwn)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='pw']")))
driver.find_element(By.XPATH, value="//*[@id='pw']").send_keys(Keys.CONTROL + 'v')
driver.find_element(By.XPATH, value="//*[@id='log.login']")


# yes 24 로그인
driver.get("http://ticket.yes24.com/Special/41862")

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='consiceLogin']")))
driver.find_element(by=By.XPATH, value="//*[@id='consiceLogin']").click()

pyperclip.copy(idy)
driver.find_element(by=By.XPATH, value="//*[@id='SMemberID']").send_keys(Keys.CONTROL + 'v')
pyperclip.copy(pwy)
driver.find_element(by=By.XPATH, value="//*[@id='SMemberPassword']").send_keys(Keys.CONTROL + 'v')
driver.find_element(by=By.XPATH, value="//*[@id='btnLogin']/span/em").click()


# 티켓팅 직전 새로고침
curr_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).time()
while float(curr_time.strftime("%H%M%S")) <= float(datetime.time(19, 59, 59, 999999).strftime("%H%M%S.%f")):
    curr_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).time()
    print(f"현재시간(UTC) : {curr_time}", end="\r")
    time.sleep(0.02)
print("")
driver.refresh()

# 티켓팅 시작
try:
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//*[@id='rncalendar']/div/table/tbody/tr[1]/td[7]/a")))
    driver.find_element(by=By.XPATH, value="//*[@id='rncalendar']/div/table/tbody/tr[1]/td[7]/a").click()

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//*[@id='mainForm']/div[10]/div/div[4]/a[4]")))
    driver.find_element(by=By.XPATH, value="//*[@id='mainForm']/div[10]/div/div[4]/a[4]").click()
except:
    pass

# da = Alert(driver)
# da.accept()

# step1 관람일/회차 선택
try:
    driver.switch_to.window(driver.window_handles[1])

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='calendar']/table/tbody/tr[3]/td[7]")))
    driver.find_element(by=By.XPATH, value="//*[@id='calendar']/table/tbody/tr[3]/td[7]").click()

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='StepCtrlBtn01']/a/img")))
    driver.find_element(by=By.XPATH, value="//*[@id='StepCtrlBtn01']/a/img").click()
except:
    pass

# while True:
#     if keyboard.read_key() == "q":
#         print("좌석선택 완료")
#         break

# step2 좌석 선택
# try:
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'ifrmSeatFrame')))
#     frame = driver.find_element_by_id('ifrmSeatFrame')
#     driver.switch_to.frame(frame)
# except:
#     pass

# driver.execute_script("javascript:ChangeBlock(2)")
# WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='StepCtrlBtn01']/a/img")))
# driver.find_element(by=By.XPATH, value="//*[@id='StepCtrlBtn01']/a/img").click()

# //*[@id="t1000072"]
# //*[@id="t400029"]

try:
    # step3
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id='StepCtrlBtn03']/a[2]/img")))
    driver.find_element(by=By.XPATH, value="//*[@id='StepCtrlBtn03']/a[2]/img").click()

    # step4
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='StepCtrlBtn04']/a[2]/img")))
    driver.find_element(by=By.XPATH, value="//*[@id='StepCtrlBtn04']/a[2]/img").click()

    # step5
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='rdoPays37433']")))
    driver.find_element(by=By.XPATH, value="//*[@id='rdoPays37433']").click()

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='cbxCancelFeeAgree']")))
    driver.find_element(by=By.XPATH, value="//*[@id='cbxCancelFeeAgree']").click()

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='chkinfoAgree']")))
    driver.find_element(by=By.XPATH, value="//*[@id='chkinfoAgree']").click()
except:
    pass

input() # 삭제금지