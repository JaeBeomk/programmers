import requests
from bs4 import BeautifulSoup
import pandas as pd

# 미세먼지 데이터 가져와서 추출 API 연습

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={
    'serviceKey' : '+CCe0/HAC20aSyFjtjCLeWmXf3YC25ZeWp6alHR3ZpE+hfoUyBhfyQv222qw24szc0n6ObiUjrhkm7uuzpKZiQ==',
    'returnType' : 'xml',
    'numOfRows' : '25',
    'pageNo' : '1',
    'sidoName' : '서울',
    'ver' : '1.0' 
}
response=requests.get(url,params=params) #REQUST로 데이터 요청하기
# print(response.text,"응답완료")

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
ItemList=soup.findAll('item')

#데이터를 담기위한 빈 리스트들! 여기에 데이터들을 하나씩 추가해 갈겁니다!
datetimeList=[] 
citynameList=[]
so2valueList=[] # 아황산가스 농도
covalueList=[] # 일산화탄소 농도
o3valueList=[] # 오존 농도
no2valueList=[] # 이산화질소 농도
pm10valueList=[] # 미세먼지(PM10) 농도
pm25valueList=[] # 초미세먼지(PM2.5) 농도


for item in ItemList:
    datetime=item.find('datatime').text 
    cityname=item.find('stationname').text
    so2value=item.find('so2value').text
    covalue=item.find('covalue').text
    o3value=item.find('o3value').text
    no2value=item.find('no2value').text
    pm10value=item.find('pm10value').text
    pm25value=item.find('pm25value').text
    
    datetimeList.append(datetime) 
    citynameList.append(cityname)
    so2valueList.append(so2value)
    covalueList.append(covalue)
    o3valueList.append(o3value)
    no2valueList.append(no2value)
    pm10valueList.append(pm10value)
    pm25valueList.append(pm25value)

print("데이터 모으기 끝!")
#데이터 합치기


# 명칭 지정 후 데이터 적재
DATA= pd.DataFrame()
DATA['time']=datetimeList
DATA['지역']=citynameList
DATA['아황산가스']=so2valueList
DATA['일산화탄소']=covalueList
DATA['오존']=o3valueList
DATA['이산화질소']=no2valueList
DATA['미세먼지(PM10)']=pm10valueList
DATA['초미세먼지(PM2.5)']=pm25valueList



DATA.to_csv("서울시_미세먼지데이터.csv",index=False,encoding="utf-8-sig")


