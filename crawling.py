import requests
from bs4 import BeautifulSoup

kakao_url = "https://careers.kakao.com/jobs"
naver_url = "https://recruit.navercorp.com/cnts/tech"
line_url = "https://careers.linecorp.com/ko/jobs?ca=Engineering&ci=Seoul,Bundang&co=East%20Asia"
coupang_url = "https://www.coupang.jobs/kr/jobs/?department=Ecommerce+Engineering&department=Play+Engineering&department=Product+UX&department=Search+and+Discovery&department=Search+and+Discovery+Core+Infrastructure&department=Cloud+Platform&department=Corporate+IT&department=eCommerce+Product&department=FTS+(Fulfillment+and+Transportation+System)&department=Marketplace%2c+Catalog+%26+Pricing+Systems&department=Program+Management+Office&department=Customer+Experience+Product"
for i in range(0, 7):
    req = requests.get(coupang_url, params={'part': 'TECHNOLOG', 'page': i})
    soup = BeautifulSoup(req.text, 'html.parser')
url = 'https://www.coupang.jobs/kr/jobs/?department=Ecommerce+Engineering&department=Play+Engineering&department=Product+UX&department=Search+and+Discovery&department=Search+and+Discovery+Core+Infrastructure&department=Cloud+Platform&department=Corporate+IT&department=eCommerce+Product&department=FTS+(Fulfillment+and+Transportation+System)&department=Marketplace%2c+Catalog+%26+Pricing+Systems&department=Program+Management+Office&department=Customer+Experience+Product'
#url = 'https://careers.kakao.com/jobs?part=TECHNOLOGY&keyword=&skilset=&page=1'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

list_area = soup.find_all('div', class_='card-body')            
link_dic = {}
            
for job in list_area:
    link = "https://www.coupang.jobs" + job.a["href"]
    title = job.find_all('a', class_='stretched-link')
    for text in title:
        title_text = text.get_text()
                # tag = job.find_all('div', class_='text_filter')
                # tags = []
                # for item in tag:
                #     tags.append(item.get_text().strip())

        link_dic[title_text] = link
print(link_dic)
#print(link_dic)