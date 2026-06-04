# 파일명은 naver_news_section.csv
# 컬럼명은 titles, category로 해주세요!
# 00님이 정치, 경제
# 01님이 사회, 문화
# 02님이 세계, IT
# 다 되면 PR 부탁드립니다!!!

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
options.add_argument('lang=ko_KR')
# 브라우져 안보이게 하기
options.add_argument('headless')

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = 'https://news.naver.com/section/100'
driver.get(url)
button_xpath = '//*[@id="newsct"]/div[4]/div/div[2]/a'
for i in range(50):
    driver.find_element(By.XPATH, button_xpath).click()
    time.sleep(0.5)

for i in range(1, 5):
    for j in range(1, 7):
        try:
            title_xpath = '//*[@id="newsct"]/div[4]/div/div[1]/div[{}]/ul/li[{}]/div/div/div[2]/a/strong'.format(i, j)
            title = driver.find_element(By.XPATH, title_xpath).text
            print(title)
        except:
            print('error', i, j)