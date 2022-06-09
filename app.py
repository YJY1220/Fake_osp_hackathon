# #!/usr/bin/python
# #-*- coding: utf-8 -*-

# import re
# import requests
# import sys
# from bs4 import BeautifulSoup
# from flask import Flask, render_template, request
# from elasticsearch import Elasticsearch

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('main.html')

# @app.route('/crawling', methods=['POST'])
# def crawling():
#     url = request.form['URL']
#     res = requests.get(url)
#     soup = BeautifulSoup(res.content, 'html.parser')
#     tb = soup.find_all('h4', {'class' : 'tit_jobs'})
#     tag = soup.find_all('span', {'class' : 'txt_hash'} )
#     lis = []
#     tib = []
#     for name in tb:
#         if(name==None):
#             break
#         lis.append(name.get_text())
#     for sub in tag:
#         if(sub==None):
#             break
#         tib.append(sub.get_text())
#     # dic = {}
#     # tobb = {}
#     es = Elasticsearch('http://localhost:9200')
#     doc = {}
#     doc['url'] = url
#     for i in lis:
#         i = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','',i)
#         doc['words'] =i
#     for r in tib:
#         r = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','',r)
#         doc['frequencies'] = r
    
#         #  word = i.split()
#         #  for w in word:
#         #      if w not in dic:
#         #          dic[w] = dic.get(w,1)
#         #      else:
#         #          dic[w] += 1
#         #  value_list = list(dic.values())
#         #  key_list = list(dic.keys())

       
#         # doc['words' : lis ]
#         # doc['frequencies': tib]
#         # doc = {
#         #      'url' : url,
#         #      'words' : lis,
#         #      'frequencies' : tib
#         #  }
#         global data
#         docs = es.index(index="web", id=1, body=doc)
#         results = es.search(index="web", body={"query":{"match_all":{}}})
#         for result in results['hits']['hits']:
#             data = result['_source']
#         return render_template('crawling.html',list=data)

# if __name__=='__main__':
#     app.run()

#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html")

@app.route('/contents', methods=['POST'])
def contents():
    error = None
    if request.method == 'POST':
        company = request.form['company']

        if (company.__eq__("kakao")):
            url = "https://careers.kakao.com/jobs"
            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'html.parser')

            list_area = soup.find_all('div', class_='wrap_info')
            res_dic = {}
            link_dic = {}
            for job in list_area:
                link = "https://careers.kakao.com" + job.a["href"]
                title = job.find_all('h4', class_='tit_jobs')
                for text in title:
                    title_text = text.get_text()
                tag = job.find_all('a', class_='link_tag')
                tags = []
                for item in tag:
                    tags.append(item.get_text().strip())

                res_dic[title_text] = tags
                link_dic[title_text] = link

            return render_template('kakao.html', result=res_dic, link=link_dic)

        if (company.__eq__("line")):
            url = "https://careers.linecorp.com/jobs?ca=Engineering&ci=Seoul,Bundang&co=East%20Asia"
            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'html.parser')

            list_area = soup.find_all('ul', class_='job_list').find_all('li')            
            res_dic = {}
            link_dic = {}
            for job in list_area:
                link = "https://careers.linecorp.com/" + job.find('a')["href"]
                title = job.find_all('h3', class_='title')
                for text in title:
                    title_text = text.get_text()
                tag = job.find_all('div', class_='text_filter')
                tags = []
                for item in tag:
                    tags.append(item.get_text().strip())

                res_dic[title_text] = tags
                link_dic[title_text] = link

            return render_template('line.html', result=res_dic, link=link_dic)

        if (company.__eq__("coupang")):
            url = "https://www.coupang.jobs/kr/jobs/?department=Ecommerce+Engineering&department=Play+Engineering&department=Product+UX&department=Search+and+Discovery&department=Search+and+Discovery+Core+Infrastructure&department=Cloud+Platform&department=Corporate+IT&department=eCommerce+Product&department=FTS+(Fulfillment+and+Transportation+System)&department=Marketplace%2c+Catalog+%26+Pricing+Systems&department=Program+Management+Office&department=Customer+Experience+Product"
            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'html.parser')

            list_area = soup.find_all('div', class_='card card-job')            
            res_dic = {}
            link_dic = {}
            for job in list_area:
                link = "https://www.coupang.jobs/" + job.a["href"]
                title = job.find_all('a', class_='stretched-link')
                for text in title:
                    title_text = text.get_text()
                # tag = job.find_all('div', class_='text_filter')
                # tags = []
                # for item in tag:
                #     tags.append(item.get_text().strip())

                #res_dic[title_text] = tags
                link_dic[title_text] = link

            return render_template('coupang.html', result=link_dic)    

if __name__=='__main__':
    app.run()