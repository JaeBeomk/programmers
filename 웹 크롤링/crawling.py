import requests
from bs4 import BeautifulSoup
import pandas as pd

# verify 옵션을 사용해야 SSLError 안나옴
resp=requests.get('https://finance.naver.com/',verify=False)
html=resp.text
soup=BeautifulSoup(html,'html.parser')

# select시 class 명으로 찾고 뛰어쓰기로 해당 태그 검색
value=soup.select('.tbl_home tbody th a')
# <a href="/item/main.naver?code=252670" onclick="clickcr(this, 'spe.slist', '252670', '1', event);">KODEX 200선물인버스2X</a>
print(value)

title = [] 
url = []
for n in value:
    # 반복으로 담을껀데 text area는 text로 나머지 옵션은 옵션명으로 추출
    title.append(n.text)
    url.append(n['href'])

df=pd.DataFrame()
df['제목'] = title
df['URL'] = url
print(df)

# csv 파일을 추출하고 한글 깨짐 방지시 utf-8이 아닌 utf-8-sig 입력 
# df.to_csv('nfinance.csv',index=False,encoding="utf-8-sig")