#!/usr/bin/python
#-*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, request, json
import requests
import re
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch

 
app = Flask(__name__)
#es_host = "http://localhost:9200"

@app.route('/')
def main():
    return render_template('main.html')

@app.route("/crawling", methods = ['POST', 'GET'])
def crawling():
    #url = 'https://careers.kakao.com/jobs'
    if request.method == 'POST':
        #response = request.get(url)
        response = requests.get(request.form["URL"])
        soup = BeautifulSoup(response.content,'html.parser')

        if "kakao" in str(request.form["URL"]):
            result_list=[]
            ex1_list=[]
            exxxx_list=[]
            # content = soup.select_one('ul.list_jobs')
            # titles = content.select('li >div > div > a')
            titles = soup.find_all('h4', {'class' : 'tit_jobs'})
            for i in titles:
                if(i==None):
                    break
                ex1_list.append(i.get_text())
            for i in ex1_list:
                exxxx_list.append(i.lower())
            
            for i in exxxx_list:
                i = re.sub('\n','',i)
                i = re.sub('\n','',i)
                i = i.split('[')

                if len(i) > 0:
                    result_list.append(i)
            
            another = soup.find_all('a', {'class' : 'link_tag'})
            atat_list=[]
            rrrr_list=[]
            final_list=[]
            for r in another:
                if(r==None):
                    break
                atat_list.append(r.get_text())
            for r in atat_list:
                rrrr_list.append(r.lower())
            
            for r in rrrr_list:
                r = re.sub('\n','',r)
                r = re.sub('\n','',r)
                r = r.split('[')

                if len(r) > 0:
                    final_list.append(r)

            #es = Elasticsearch(es_host)

            # dic = []
            # for i in result_list:
            #     dic.append({"word" : i})
                #res = es.
            # for title in titles:
            #     if(title==None):
            #         break
            #     result_list.append(title.get_text())
        elif "navercorp" in str(request.form["URL"]):
            result_list=[ ]
            # content = soup.find('div', class_ = 'card_list')
            # midd = content.select('ul > li > a > span')
            titles = soup.find_all('strong', {'class' : 'crd_tit'})
            for title in titles:
                if(title==None):
                    break
                result_list.append(title.get_text())
        elif "linecorp" in str(request.form["URL"]):
            result_list=[]
            uuuu_list = []
            qqqq_list = []
            titles = soup.find_all('ul', {'class' : 'job_list'})

            for i in titles:
                if(i==None):
                    break
                uuuu_list.append(i.get_text())
            for i in uuuu_list:
                qqqq_list.append(i.lower())
            
            for i in qqqq_list:
                i = re.sub('\n','',i)
                i = re.sub('\n','',i)
                #i = i.split('까지')
                if len(i) > 0:
                    result_list.append(i)
        elif "coupang" in str(request.form["URL"]):
            result_list=[]
            pppp_list=[]
            oooo_list=[]

            titles = soup.find_all('div', {'class' : 'card card-job'})

            for i in titles:
                if(i==None):
                    break
                pppp_list.append(i.get_text())
            for i in pppp_list:
                oooo_list.append(i.lower())
            for i in oooo_list:
                i = re.sub('\n','',i)
                i = re.sub('\n','',i)
                i = re.sub('저장하기저장 완료서울','',i)
                i = re.sub('저장하기저장 완료서울','',i)

                if len(i) > 0:
                    result_list.append(i)
        elif "toss" in str(request.form["URL"]):
            result_list=[]
            aaaa_list=[]
            bbbb_list=[]

            titles = soup.find_all('div', {'class' : 'css-1xr69i7'})
            for i in titles:
                if(i==None):
                    break
                aaaa_list.append(i.get_text())
            for i in aaaa_list:
                bbbb_list.append(i.lower())
            for i in bbbb_list:
                i = re.sub('\n','',i)
                i = re.sub('\n','',i)
                # i = re.sub('저장하기저장 완료서울','',i)
                # i = re.sub('저장하기저장 완료서울','',i)

                if len(i) > 0:
                    result_list.append(i)
        elif "woowahan" in str(request.form["URL"]):
            result_list=[]
            aaaa_list=[]
            bbbb_list=[]

            titles = soup.find_all('div', {'class' : 'recruit-list'})
            for i in titles:
                if(i==None):
                    break
                aaaa_list.append(i.get_text())
            for i in aaaa_list:
                bbbb_list.append(i.lower())
            for i in bbbb_list:
                i = re.sub('\n','',i)
                i = re.sub('\n','',i)
                #i = re.sub('당근페이','',i)

                if len(i) > 0:
                    result_list.append(i)
                #issue 사용법 종료   
        else:
            print(response.status_code)

    return render_template('crawling.html', response = result_list, allres = final_list)


if __name__=="__main__":
    app.run()


# #!usr/bin/python3
# # -*- coding: utf-8 -*-

# import re
# import requests
# from bs4 import BeautifulSoup
# from flask import Flask, render_template, request, json
# from elasticsearch import Elasticsearch

# app = Flask(__name__)
# es_host = "http://127.0.0.1:9200"


# @app.route('/', methods=['GET'])
# def home():
#     return render_template('home.html')


# @app.route('/crawl')  # , methods=['GET', 'POST'])
# def crawl():
#     if request.method == 'GET':
#         url = request.args.get("url")

#         if url == 'https://en.wikipedia.org/wiki/Web_crawler ' or url == 'https://en.wikipedia.org/wiki/NoSQL':
#             page = requests.get(url)

#             soup = BeautifulSoup(page.content, 'html.parser')

#             tb = soup.find_all('p')
#             tb = tb + soup.find_all('span', class_="mw-headline")
#             tb = tb + soup.find_all('cite', class_="citation")

#             s = ""
#             for t in tb:
#                 s = s + t.get_text()

#             s = re.sub("<>.", '', s, 0).strip()
#             s = re.sub('[-=+,#/\?:;^.@*\"※~ㆍ!‘|\(\)\[\]`\'…\”\“\’·  ]', ' ', s)

#             list = s.split()
#             wordList = []
#             countList = []

#             for i in list:
#                 if i in wordList:
#                     countList[wordList.index(i)] = countList[wordList.index(i)] + 1
#                 else:
#                     wordList.append(i)
#                     countList.append(1)

#             es = Elasticsearch(es_host)

#             dic = []
#             for i in wordList:
#                 dic.append({"url": url, "word": i, "frequency": str(countList[wordList.index(i)])})
#                 res = es.index(index="web", id=wordList.index(i), document=dic[wordList.index(i)])

#             return render_template('resultpage.html', link=url, wordlist=wordList, countlist=countList)
#         else:
#             return "this URL is not Supporting"
#     else:
#         return "this URL is not Supporting"


# if __name__ == "__main__":
#     app.run(debug=True)