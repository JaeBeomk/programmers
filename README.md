# programmers Study
# someday practice algorithm for python
list 배열의 합은 sum 함수로 합쳐진다. 
for 반복문을 배열에서 사용시 range(len())는 길이만큼 in은 배열안의 인덱스를 반복이다 

2023.11.24 
배열 뒤집기 사용시 num_list 리스트 배열이라고 치면 num_list.reverse() 를 사용하거나 list(reversed(num_list))를 사용 하면된다.

2023.11.27 
문자열 뒤집기는 슬라이싱이 깔끔한 코드로 보이며
반복문 출력시 배열의 크기만큼 반복을 할것인지, 배열내의 index를 반복할것인지를 잘 이해해야할것같다.

2023.11.30 
python 조건문 한줄 A if 조건 else B
배열의 index()는 괄호안의 값을 입력했을때 그 값의 위치를 알려준다. 반대로

2023.12.06-07
python f-String 사용값을 계산해주는 eval 함수를 이용해보자
f-string이란? => 문자열 맨 앞에 f를 붙여주고, 중괄호 안에 직접 변수 이름이나 출력하고 싶은것을 바로 넣기
f'문자열 {변수} 문자열'

2023.12.08 
배열의 마지막값을 가져오는건 [-1]을 사용

2023.12.11 
문자열 포함을 찾으려면 in 함수 사용
maketrans('ab','cd') 는 a는c b는d로 변경이다. 객체를 만들어 담아주고 translate로 변경해주면된다. 

2023.12.14-15
제곱 세제곱은 a**2 a**3과 같이 표기한다.

2023.12.16 
set함수는 list의 중복을 제거한 집합을 만들어 연산에 사용된다.

2023.12.19
배열을 나선형으로 집어넣으려니.... 마땅한 방법이 떠오르지는 않고 이차원 배열을 돌리는게 정답이라니... 참... 게시판이나 만들어야지...ㅎㅎㅎ

2023.12.20-21
django page 보이기 성공

2024.01.05 회사 github연동 성공
- DB migrate
python manage.py makemigrations
python manage.py migrate
- superuser 생성
python manage.py createsuperuser
username
email
password
게시글 생성 후 blog.html 에 mvc가 잘 연결되었나 확인

2024.01.08
확인은 아직도 안했지만... posting_page 추가해서 pk값으로 post가져와서 보여주기 및 문제 몇개 해결 + kube yaml 생성

2024.01.12-15
image 설정
pip install pillow
python manage.py makemigration
python manage.py migrate
python manage.py runserver
완료(작업트리는 뭐야)

2024.01.16-17
계산기를 한번 만들어봤는데 popup을 이용한 tkinter 라이브러리는 참신한것같다. 
이걸 활용해서 뭔가 더 만들어 볼수 있겠다

2024.01.23
n의 제곱근은 sqrt= n**(1/2) 으로 구할수있었다....
sorted와 reversed함수는 리스트만 가능

2024.02.05 
list의 각 요소 형변환
{담을것}=list(map(int,{리스트}))

2024.02.06
나머지 해결 새로운 프로젝트 고민

2024.02.07
문자열 역순
-1 s[::-1] # 문자열 슬라이싱
-2 r=reversed(s) # 리버스 문법에 담아 메모리에 담긴거 확인 후 출력
   print(''.join(r))

2진수 변환은 bin() 내장함수 사용하기

django 프로젝트에서 vc연동시 저장을 생활화 하자....ㅠ


2024.02.08
txt 파일 자동 줄바꿈 Alt+z
sqlite3 / django 설치 사내망 테스트 완료

2024.02.21
django Template에서 변수를 출력하고자할때 {{변수}} 를 사용
태그= {% %}
django의 이미지 처리는 pillow 라이브러리 설치 필요

2024.03.03
admin페이지의 이미지 처리를 위해 설치
pip install 'django-admin-thumbnails<0.3'

2024.03.05
배열의 중복요소 제거= set() 함수
합집합은 s1 | s2
교집합은 s1 & s2 or s1.intersection(s2)

2024.03.06
image 가 안보이는건 둘째고...css도 적용안됨?
댓글 기능 동작 확인해보자

2024.03.07
k8s ns deploy 입력해 해당 deploy 네임의 pod의 컨테이너별 resource %

2024.03.08
insert키만 누르면 뒤에 글자 수정됨

2024.03.09
314
크롤링 해보기
쿠버네티스 구축 따라해 보기
https://syhwang.tistory.com/43?category=1220695