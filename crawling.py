# # # import requests
# # # from bs4 import BeautifulSoup
# # # import time
# # # import re
# # # import pprint
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from webdriver_manager.chrome import ChromeDriverManager
# # # from elasticsearch import Elasticsearch

# # # es = Elasticsearch('http://localhost:9200')

# # # kakao_url = "https://careers.kakao.com/jobs"
# # # naver_url = "https://recruit.navercorp.com/cnts/tech"
# # # line_url = "https://careers.linecorp.com/ko/jobs?ca=Engineering&ci=Seoul,Bundang&co=East%20Asia"
# # # coupang_url = "https://www.coupang.jobs/kr/jobs/?department=Ecommerce+Engineering&department=Play+Engineering&department=Product+UX&department=Search+and+Discovery&department=Search+and+Discovery+Core+Infrastructure&department=Cloud+Platform&department=Corporate+IT&department=eCommerce+Product&department=FTS+(Fulfillment+and+Transportation+System)&department=Marketplace%2c+Catalog+%26+Pricing+Systems&department=Program+Management+Office&department=Customer+Experience+Product"
# # # woowahan_url = "https://career.woowahan.com/?jobCodes&employmentTypeCodes=&serviceSectionCodes=&careerPeriod=&keyword=&category=jobGroupCodes%3ABA005001#recruit-list"
# # # daangn_url = "https://team.daangn.com/jobs/"

# # # url = 'https://team.daangn.com/jobs/'
# # # req = requests.get(url)
# # # soup = BeautifulSoup(req.text, 'html.parser')

# # # list_area = soup.find('div', class_=False)            
# # # link_dic = {}
            
# # # for job in list_area.find_all('li', class_="c-deAcZv"):
# # #     link = "https://team.daangn.com/jobs" + job.a["href"]
# # #     title = job.find_all('h3', class_='c-boyXyq')
# # #     for text in title:
# # #         title_text = text.get_text()

# # #         link_dic[title_text] = link

# # # def insert(body):
# # #     return es.index(index=index, doc_type=doc_type, body=body)
    
# # # def search(index, data=None):
# # #     if data is None:
# # #         data = {"match_all": {}}
# # #     else:
# # #         data = {"match": data}
    
# # #     body = {"query": data}
# # #     res = es.search(index=index, body=body)
# # #     return res

# # # index = 'employment'
# # # doc_type = 'daangn'
# # # data ={
# # #     'title': '',
# # #     'content': '',
# # #     'url': ''
# # # }

# # # sr = search(index)
# # # pprint.pprint(sr)
# import re
# import requests
# import sys
# import pprint
# from bs4 import BeautifulSoup
# from flask import Flask, render_template, request
# from elasticsearch import Elasticsearch

# es = Elasticsearch('http://localhost:9200')

# # field = ["tech", "design", "service", "client"]
# # company = ["c1", "c2", "c3"]
# # job_dic = {"c1":["job1", "job2", "job3"], "c2":["job4", "job5"]}

# # # index랑 doc_type차이점

# # for job in job_dic.keys():
# #     print(job)
# #     print(job_dic[job])
    
# kakao_url = "https://careers.kakao.com/jobs"
# res_dic = {}
# link_dic = {}
# for i in range(1, 7):
#     url = kakao_url + "?page=" + str(i)
#     req = requests.get(url)
#     soup = BeautifulSoup(req.text, 'html.parser')
#     list_area = soup.find_all('div', class_='wrap_info')
#     for job in list_area:
#         link = "https://careers.kakao.com" + job.a["href"]
#         title = job.find('h4', class_='tit_jobs').text
#         tag = job.find_all('a', class_='link_tag')
#         tags = []
#         for item in tag:
#             tags.append(item.get_text().strip())

#         res_dic[title] = tags
#         link_dic[title] = link

# def insert(body):
#     #es.indices.create("employment")s
#     es.index(index=indexs, body=body)
    
# def search(indexs, data=None):
#     if data is None:
#         data = {"match_all": {}}
#     else:
#         data = {"match": data}
    
#     body = {"query": data}
#     res = es.search(index=indexs, body=body)
#     return res

# indexs = 'employment'
# data ={
#     'title': '',
#     'tags': '',
#     'content': '',
#     'url': ''
# }

# # for job in res_dic.keys():
# #     data['title'] = job
# #     data['tags'] = res_dic[job]
# #     data['url'] = link_dic[job]
# #     ir = insert(data)
    
# #     print(ir)
# insert(data)
# sr = search(indexs)
# pprint.pprint(sr)

import re
import requests
import sys
import pprint
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

field = ["tech", "design", "service", "client"]
company = ["c1", "c2", "c3"]
job_dic = {"c1":["job1", "job2", "job3"], "c2":["job4", "job5"]}

# index랑 doc_type차이점

for job in job_dic.keys():
    print(job)
    print(job_dic[job])
    
kakao_url = "https://careers.kakao.com/jobs"
res_dic = {}
link_dic = {}
for i in range(1, 7):
    url = kakao_url + "?page=" + str(i)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    list_area = soup.find_all('div', class_='wrap_info')
    for job in list_area:
        link = "https://careers.kakao.com" + job.a["href"]
        title = job.find('h4', class_='tit_jobs').text
        tag = job.find_all('a', class_='link_tag')
        tags = []
        for item in tag:
            tags.append(item.get_text().strip())

        res_dic[title] = tags
        link_dic[title] = link

def insert(body):
    return es.index(index=index, doc_type=doc_type, body=body)
    
def search(index, data=None):
    if data is None:
        data = {"match_all": {}}
    else:
        data = {"match": data}
    
    body = {"query": data}
    res = es.search(index=index, body=body)
    return res

index = 'employment'
doc_type = 'kakao'
data ={
    'title': '',
    'tags': '',
    'url': ''
}

for job in res_dic.keys():
    data['title'] = job
    data['tags'] = res_dic[job]
    data['url'] = link_dic[job]
    ir = insert(data)
    
    print(ir)

sr = search(index)
pprint.pprint(sr)