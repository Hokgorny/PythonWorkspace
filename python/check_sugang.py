from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://e-onestop.pusan.ac.kr/menu/class/C03/C03001?menuId=2000030301&rMenu=03")

select_subinfo = Select(driver.find_element(by=By.XPATH, value=("//*[@id='subject_is']")))
select_subinfo.select_by_value("//*[@id='refinementAndMajor']/option[22]")

select_major = Select(driver.find_element(by=By.XPATH, value=("//*[@id='subject_is']")))
select_major.select_by_value("//*[@id='refinementAndMajor']/option[22]")

driver.find_element(by=By.XPATH, value=("//*[@id='search']")).click()


jehan = driver.find_element(by=By.XPATH, value=("//*[@id='jehan']/tr[1]/td[2]"))