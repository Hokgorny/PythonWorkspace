# # 디시인사이드 개추 주작기


# # 1. 게시글 주소 입력
# # 2. 필요한 엘리먼트 가져오기(+자동입력방지문자 존재 유무 확인)
# ## Loop
# # # 3. 아이피 바꾸기 (proxy rotating)
# # # 4 - 1. 자동입력방지문자 존재시, ocr사용 후 입력(부재시 바로 4 - 2)
# # # 4 - 2. 개추 클릭
# # ## Loop/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#driver.implicitly_wait(3) # 암묵적으로 웹 자원 로드를 위해 3초 기다림

driver.get('https://naver.com')

elem = driver.find_elements_by_tag_name("a")
print(elem)

input()