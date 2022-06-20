import requests
from bs4 import BeautifulSoup
import time
import re
import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch('http://localhost:9200')


# index랑 doc_type차이점

 
index = 'employment'
doc_type = 'daangn'
data = {
    'title': '',
    'url': ''
    }

def insert(body):
    return es.index(index=index, body=body)

kakao_url = "https://careers.kakao.com/jobs"
naver_url = "https://recruit.navercorp.com/cnts/tech"
line_url = "https://careers.linecorp.com/ko/jobs?ca=Engineering&ci=Seoul,Bundang&co=East%20Asia"
coupang_url = "https://www.coupang.jobs/kr/jobs/?department=Ecommerce+Engineering&department=Play+Engineering&department=Product+UX&department=Search+and+Discovery&department=Search+and+Discovery+Core+Infrastructure&department=Cloud+Platform&department=Corporate+IT&department=eCommerce+Product&department=FTS+(Fulfillment+and+Transportation+System)&department=Marketplace%2c+Catalog+%26+Pricing+Systems&department=Program+Management+Office&department=Customer+Experience+Product"
woowahan_url = "https://career.woowahan.com/?jobCodes&employmentTypeCodes=&serviceSectionCodes=&careerPeriod=&keyword=&category=jobGroupCodes%3ABA005001#recruit-list"
daangn_url = "https://team.daangn.com/jobs/"
url = 'https://team.daangn.com/jobs/'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

list_area = soup.find('div', class_=False)            
link_dic = {}
            
for job in list_area.find_all('li', class_="c-deAcZv"):
    link = "https://team.daangn.com/jobs" + job.a["href"]
    title = job.find_all('h3', class_='c-boyXyq')
    for text in title:
        title_text = text.get_text()

        link_dic[title_text] = link

for job in link_dic.keys():
    data['title'] = job
    data['url'] = link_dic[job]
    ir =insert(data)

