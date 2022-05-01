# 부산대학교 수강신청 툴
# 1. 수강신청 로그인 페이지 진입
# 2. 수강신청 페이지 진입할 때까지 로그인 버튼 반복 클릭 
# 3. 수강신청 페이지 진입 후, 희망과목 수강신청 버튼 클릭

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 수강신청 로그인 페이지 진입
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome("./chromedriver.exe" , options=options)
driver.get("https://sugang.pusan.ac.kr/sugang/Login.aspx")


# 2. 수강신청 페이지 진입할 때까지 로그인 버튼 반복 클릭
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtid']")))
driver.find_element_by_xpath("//*[@id='txtid']").send_keys("201827148")

while driver.current_url != "https://sugang.pusan.ac.kr/sugang/Sugang-insert.aspx":
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtid']")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtpassword']")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='btnlogin']")))
    driver.find_element_by_xpath("//*[@id='txtpassword']").send_keys("msh46282651**")
    driver.find_element_by_xpath("//*[@id='btnlogin']").click()

# 3. 수강신청 페이지 진입 후, 희망과목 수강신청 버튼 클릭
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@id,'_bt신청')]")))
subjects = driver.find_elements_by_xpath("//*[contains(@id,'_bt신청')]")

for i in range (0, len(subjects)-1):
    subjects[i].click()
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@id,'_bt신청')]")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='lbError']")))
    subjects = driver.find_elements_by_xpath("//*[contains(@id,'_bt신청')]")
    res = driver.find_element_by_xpath("//*[@id='lbError']")
    print(f"{i}번째 과목 : {res.text}\n")



# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl02_bt신청']")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl03_bt신청']")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl04_bt신청']")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl05_bt신청']")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl06_bt신청']")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl07_bt신청']")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl08_bt신청']")))
# subjects = driver.find_elements_by_xpath("//*[contains(@id,'_bt신청')]")
# for i in range(0, len(subjects) - 1):
#     subjects[i].click()
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl02_bt신청']")))
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl03_bt신청']")))
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl04_bt신청']")))
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl05_bt신청']")))
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl06_bt신청']")))
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl07_bt신청']")))
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dgBasket_List_ctl08_bt신청']")))
#     subjects = driver.find_elements_by_xpath("//*[contains(@id,'_bt신청')]")

# 3. 수강신청 페이지 진입 후, 희망과목 수강신청 버튼 모두 클릭
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@id,'_bt신청')]")))
# subjects = driver.find_elements_by_xpath("//*[contains(@id,'_bt신청')]")
# for subject in subjects:
#     try:
#         subject.click()
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@id,'_bt신청')]")))
#         subjects = driver.find_elements_by_xpath("//*[contains(@id,'_bt신청')]")
#     except StaleElementReferenceException:
#         print("이미 수강신청 완료된 과목입니다.")

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@id,'_bt신청')]")))
# subjects = driver.find_elements_by_xpath("//*[contains(@id,'_bt신청')]")
# print(len(subjects))
# i = 1
# num_of_subject = len(subjects)
# while i <= num_of_subject - 3:
#     try:
#         subjects[i + 3].click()
#     except StaleElementReferenceException:
#         print("이미 수강신청 완료된 과목입니다.")
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@id,'_bt신청')]")))
#         subjects = driver.find_elements_by_xpath("//*[contains(@id,'_bt신청')]")
#         print(subjects)
#         print(subjects[i])

# subjects = driver.find_elements_by_xpath("//*[contains(@id,'_bt신청')]")

# i = 1
# num_of_subjects = len(subjects)
# while i <= num_of_subjects:
#     WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@id,'_bt신청')]")))
#     if i == 4 or 5:
#         subjects[i].click()

# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='dgBasket_List_ctl05_bt신청']")))
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='dgBasket_List_ctl06_bt신청']")))
# subjects = driver.find_elements_by_xpath("//*[contains(@id,'_bt신청')]")
# for subject in subjects:
#     subject.click()
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='dgBasket_List_ctl05_bt신청']")))
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='dgBasket_List_ctl06_bt신청']")))
#     subjects = driver.find_elements_by_xpath("//*[contains(@id,'_bt신청')]")