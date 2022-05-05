import requests
from bs4 import BeautifulSoup
import datetime
date = datetime.datetime.today()

# 웹페이지 불러오기
url = "https://music.bugs.co.kr/chart"
response = requests.get(url)

'''
file = open("bugs.html", "w")
file.write(response.text)
file.close
'''

# text 파싱
soup = BeautifulSoup(response.text, 'html.parser')


results = soup.findAll("p","title")
rank =1

search_rank_file = open("practice1.txt", "w")

# 시간, 순위, 내용
for result in results:
    search_rank_file.write(str(date)+"의 벅스 실시간 차트 순위입니다."+"\n"+"\n"+str(rank)+"위:"+"\n"+result.get_text()+"\n"+"\n")
    # print(rank, "위: ")
    # print(result.get_text(), '\n')
    rank += 1