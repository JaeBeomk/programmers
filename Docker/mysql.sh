sudo -i

# 환경변수 사용해 데이터 전달
docker run -d --name nx -e env_name=test1234 nginx

# MySQL 서비스 구축
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD='!qhdkscjfwj@' -d mysql

# 컨테이너 구동 확인 
docker ps -a

# MySQL 접속
$ docker exec -it some-mysql mysql
# password: !qhdkscjfwj@
