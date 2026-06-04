# 파일명은 naver_news_section.csv
# 컬럼명은 titles, category로 해주세요!
# 영재님이 정치, 경제
# 유정님이 사회, 문화
# 도영님이 세계, IT
# 다 되면 PR 부탁드립니다!!!


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time


category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']
df_titles = pd.DataFrame()

options = ChromeOptions()
options.add_argument('lang=ko_KR')
# 브라우져 안보이게 하기
options.add_argument('headless')

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

button_xpath = '//*[@id="newsct"]/div[4]/div/div[2]/a'

# 도영 담당: World(104), IT(105)
for SECTION, CATEGORY in zip(range(4, 6), category[4:6]):
    url = 'https://news.naver.com/section/10{}'.format(SECTION)
    driver.get(url)

    # 더보기 클릭
    for i in range(30):
        driver.find_element(By.XPATH, button_xpath).click()
        time.sleep(0.5)

    titles = []
    for j in range(1, 180):
        for k in range(1, 7):
            try:
                title_xpath = '//*[@id="newsct"]/div[4]/div/div[1]/div[{}]/ul/li[{}]/div/div/div[2]/a/strong'.format(
                    j, k)
                title = driver.find_element(By.XPATH, title_xpath).text
                titles.append(title)
            except:
                print('error', j, k)

    df_section_titles = pd.DataFrame(titles, columns=['titles'])
    df_section_titles['category'] = CATEGORY

    df_titles = pd.concat([df_titles, df_section_titles], ignore_index=True)

driver.quit()
print(df_titles.head())
df_titles.info()
df_titles.to_csv('./data/naver_news_section_PDY.csv', index=False)
