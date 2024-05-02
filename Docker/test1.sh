# 도커 연습문제
# image = jenkins/jenkins:lts-jdk11

# 1. 기존에 설치된 모든 컨테이너와 이미지 정지 및 삭제
sudo docker stop `sudo docker ps -a -q`
sudo docker rm `sudo docker ps -a -q`
sudo docker rmi `sudo docker images -q`

# 2. 도커 기능을 사용해 Jenkins 검색
sudo docker search jenkins

# 3. Jenkins를 사용하여 설치
sudo docker pull jenkins
sudo docker inspect jenkins
sudo docker run -d -p 8080:8080 --name jk jenkins/jenkins:lts-jdk11 test

# 4. Jenkins 포트로 접속하여 웹 서비스 열기
firefox 127.0.0.1:8080

# 5. Jenkins의 초기 패스워드 찾아서 로그인하기
sudo docker exec -it jk cat /var/jenkins_home/secrets/initialAdminPassword
sudo docker logs jk


