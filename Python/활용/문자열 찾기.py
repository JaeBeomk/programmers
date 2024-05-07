# find 함수 
# find함수는 있으면 위치를 없으면 -1 return
comp_data = '삼성전자,LG전자,현대자동차,CJ,SK텔레콤'

print(comp_data.find('네이버'))

# index 함수
# index함수는 있으면 위치를 없으면 ValueError를 return 하므로 try except 구문 사용
comp_data = '삼성전자,LG전자,현대자동차,CJ,SK텔레콤'

try:
    print(comp_data.index('네이버'))
except ValueError:
    print(-1)
