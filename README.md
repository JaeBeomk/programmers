# programmers Study
# practice anything
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
공통 화면 내용 템플릿 분기


2024.03.10
git push error - > file 용량이 큼

2024.03.11
jdk 설치
lombok extention 추가
postman 설치
ec2  instance 생성

2024.03.12
POD와 APP간 통신이 안되거나 기동이 정상이지 않을경우 확인사항 정리

2024.03.24
CKA 취득

2024.03.26
웹크롤링 연습

2024.03.27
javascript를 다시 해보자
https://nodejs.org/en/download/ 설치부터

2024.03.29
미세먼지가 심한 오늘 api로 미세먼지를 가져오고 싶다...
공공데이터 포털 = https://www.data.go.kr/ 

2024.03.31
ec2 pem키 연결 확인
https://launchpad.net/ubuntu/+ppas => apt 저장소 없는 프로그램 찾기
todo/guestbook 프로젝트 삭제
-> 새로 만들어볼 예정

2024.04.02
방명록 프로젝트 시작

2024.04.03
sqlite3의 sequence 보장을 해결하기 위한 queryset의 last pk값을 가져와 1더하기

2024.04.09
java - 삭제
toy 프로젝트 GUI 숫자야구

2024.04.14
docker 맛보기

2024.04.15
정처기 start
숫자야구 command 버전 완성
while True: 는 python2 에서는 True가 정의가 되어있지않아 1로 하는게 더 성능이 빠르다.

2024.04.18
gcp-vm-kubeadm install

2024.04.23
gcp master node kubeadm install and Node network connection

2024.04.27
정처기 ...out

2024.04.29
폴더 구조 변경 
gcp add-on설치
cluster 재 구축 집가서 함더...
externer-IP가 보이지 않는다...

2024.04.30
external-IP 해결 vpc 생성
VM 외부 통신 확인...

2024.05.07
rc(ReplicationController) 는 label selector에 따라 동작한다.
label 변경시 pod를 새로 생성하고 label 변경된 pod는 동작하지만 label selector로 연결된 서비스는 불가하다...

2024.05.13
yaml 파일 작성시 
(---)을 사용해 붙혀서 한번에 관리 가능

2024.05.16
etcd 저장소를 이용해 내용을 저장
모든 내용은 key : value 형태로 불러올수있다.
yaml파일의 형식중 ports 와 같은 복수 형태는 
'-'를 활용해 내용의 시작을 표시하며 한 묶음처럼 본다.
용량이 점차 증가하면 github 분리예정

2024.05.17
LB_tomcat_deploy.yaml
파일 작성 후 노드포트 서비스

2024.05.20
GKE로 클러스터 전환 -> LoadBalancer svc와 NodePort를 오픈 확인

2024.05.28
python 으로 bitcoin열심히 매수해보자
현재 IP만 가능

2024.05.31
liveness/readiness probe의 개념 다시 확인
gce 영구 스토리지는 명령어 혹은 콘솔로 생성 후 볼륨만 별도 선언 불가로 POD 생성해 volume 구성


2024.06.04
Network File System(NFS)
pod의 emptydir 부분을 nfs로 변경해 폴더 연동

GCE compute engine의 스토리지 디스크는 k8s공식 docs에는 서비스 제공을 중지하여서 pv/pvc/pod순으로 mount 해줘야 한다.

2024.06.05
gcp - new project(end-20240715)
vm 설치 후 k8s 세팅 완료
ssh 연동 완료
kubernetes - 자동완성

2024.06.06
django project 생성 후 git clone
image 빌드 후 pod 생성


2024.06.11
스티커메모가 연동 실패로 인해 데이터 유실...?
백업 데이터 확인 필요
sticy note -> onenote 이전 예정
onenote 내용 정리
office365종료로 일기장 변경...
프로젝트 유저 추가
그룹으로 관리 예정
github 유저추가
discord 추가

2024.06.12
mariadb 연동하는 deploy 추가
그런데 pod 삭제시 해당 db의 내용이 삭제되어서
statefulset으로 기동예정

2024.06.13
statefulset으로 기동완료
작업 후 ns를 생성해 서비스 단위 구분예정
접근 규칙 role 생성예정
DB user1~3 생성 요청
생성한 user 권한 부여 후 작업

2024.06.14


273







