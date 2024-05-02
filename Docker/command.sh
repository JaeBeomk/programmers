# Docker 설치
# 필수 ! VMware에 Linux가 설치되어있어야한다.

sudo apt install docker.io

# 도커 퍼블릭 레지스트리 검색 및 확인
# https://hub.docker.com/

# 명령어로 이미지 검색
sudo docker search tomcat

# 이미지 다운로드
sudo docker pull consol/tomcat-7.0

# 이미지 확인
sudo docker images

# 이미지 삭제
sudo docker rmi consol/tomcat-7.0

# tomcat 컨테이너 생성
sudo docker run -d --name [name] consol/tomcat-7.0

# 기동 확인
sudo docker ps
-a 옵션은 전체 확인

# 컨테이너 중지  
sudo docker stop [container id]

# 컨테이너 삭제 => 컨테이너 중지 후 삭제
sudo docker rm [container id]

# image 저장소 위치 확인
sudo docker info
저장소는 root 만 가능

# 포트포워딩 tomcat 기동
sudo docker run -d --name tc -p 80:8080 tomcat

# 컨테이너 내부 접속
sudo docker exec -it tc /bin/bash

# 컨테이너 로그 확인
sudo docker logs tc

# 도커 컨테이너 전체 삭제
sudo docker stop `sudo docker ps -a -q`
sudo docker rm `sudo docker ps -a -q`

# 임시 컨테이너 생성
sudo docker run -d -p 80:8080 --rm --name tc consol/tomcat-7.0