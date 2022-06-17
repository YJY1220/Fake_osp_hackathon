import requests
from bs4 import BeautifulSoup
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

kakao_url = "https://careers.kakao.com/jobs"
naver_url = "https://recruit.navercorp.com/cnts/tech"
line_url = "https://careers.linecorp.com/ko/jobs?ca=Engineering&ci=Seoul,Bundang&co=East%20Asia"
coupang_url = "https://www.coupang.jobs/kr/jobs/?department=Ecommerce+Engineering&department=Play+Engineering&department=Product+UX&department=Search+and+Discovery&department=Search+and+Discovery+Core+Infrastructure&department=Cloud+Platform&department=Corporate+IT&department=eCommerce+Product&department=FTS+(Fulfillment+and+Transportation+System)&department=Marketplace%2c+Catalog+%26+Pricing+Systems&department=Program+Management+Office&department=Customer+Experience+Product"

url = "https://career.woowahan.com/?jobCodes&employmentTypeCodes=&serviceSectionCodes=&careerPeriod=&keyword=&category=jobGroupCodes%3ABA005001#recruit-list"
driver = webdriver.Chrome(executable_path = 'C:\\chromedriver_win32\\chromedriver')
driver.get(url)
driver.implicitly_wait(5)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
      driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
      time.sleep(0.1)
      new_height = driver.execute_script("return document.documentElement.scrollHeight")

      if new_height == last_height:
        break
      else:
        last_height = new_height

        new_height = last_height

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        list_area = soup.find_all('ul', class_='recruit-type-list')
        res_dic = {}
        link_dic = {}
        for job in list_area:
            show = job.a["onclick"]
            show_number = re.sub(r'[^0-9]', '', show)
            link = "https://career.woowahan.com/?jobCodes&employmentTypeCodes=&serviceSectionCodes=&careerPeriod=&keyword=&category=jobGroupCodes%3ABA005001#recruit-list"
            title = job.find('p', class_='fr-view').text
            tag = job.find_all('div', class_='flag-tag')
            tags = []
            for item in tag:
                tags.append(item.get_text().strip())

        res_dic[title] = tags
        link_dic[title] = link
print(link_dic)
#print(link_dic)