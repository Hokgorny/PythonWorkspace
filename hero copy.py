from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import pyperclip

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://ticket.yes24.com/Perf/41852")

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='consiceLogin']")))
driver.find_element(by=By.XPATH, value="//*[@id='consiceLogin']").click()

id = "123kbg"
pw = "258qudrjs@"

pyperclip.copy(id)
driver.find_element(by=By.XPATH, value="//*[@id='SMemberID']").send_keys(Keys.CONTROL + 'v')
pyperclip.copy(pw)
driver.find_element(by=By.XPATH, value="//*[@id='SMemberPassword']").send_keys(Keys.CONTROL + 'v')
driver.find_element(by=By.XPATH, value="//*[@id='btnLogin']/span/em").click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='rncalendar']/div/table/tbody/tr[5]/td[7]/a")))
driver.find_element(by=By.XPATH, value="//*[@id='rncalendar']/div/table/tbody/tr[5]/td[7]/a").click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='mainForm']/div[10]/div/div[4]/a[4]")))
driver.find_element(by=By.XPATH, value="//*[@id='mainForm']/div[10]/div/div[4]/a[4]").click()

# da = Alert(driver)
# da.accept()

driver.switch_to.window(driver.window_handles[1])

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='calendar']/table/tbody/tr[6]/td[7]")))
driver.find_element(by=By.XPATH, value="//*[@id='calendar']/table/tbody/tr[6]/td[7]").click()


input()