import requests 
from bs4 import BeautifulSoup
import csv

# taget URL 
# 현재 네이버 웹툰인기순위 만들기
url = "https://comic.naver.com/webtoon/weekday"

# 웹서버에 get 요청 보내기
res= requests.get(url)
res.raise_for_status() # 정상 200

# soup 객체만들기
soup = BeautifulSoup(res.text,"lxml")

# 전체 영역에서 실시간인기웹툰 영역으로 범위 제한
box=soup.find_all('ul',attrs={"class":"AsideList__content_list--FXDvm"})


# Excel파일로 저장
filename= "네이버 웹툰 순위.csv"
f=open(filename,"w",encoding="utf-8-sig",newline="")
writer=csv.writer(f)

# 컬럼 만들기
columsName=["순위","이름"]
writer.writerow(columsName)

i=1
# 반복문으로 제목 가져오기
for i in box:
    title = box.get("ContentTitle__title_area--x24vt")
    print(f"{str(i)}위:{title}")
    data=[str(i),title]
    writer.writerow(data)
    i+=1
