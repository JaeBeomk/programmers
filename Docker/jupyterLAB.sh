sudo -i

# 볼륨 마운트 옵션 사용해 로컬 파일 공유
docker run -v <호스트 경로>:<컨테이너 내 경로>:<권한>
docker run -v  /tmp:home/user:ro

# 권한 종류 
# ro: 읽기 전용 
# rw: 읽기 쓰기

# nginx 볼륨 마운트
docker run -d -p 80:80 --rm -v /var/www:/usr/share/nginx/html:ro nginx
curl 127.0.0.1
echo 1234 > /var/www/index.html
curl 127.0.0.1
# index page 변경 확인

# jupyter LAB환경 구축
mkdir ~/jupyternotebook
chmod 777 ~/jupyternotebook
cd ~/jupyternotebook
docker run --rm -p 8080:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work:rw jupyter/datascience-notebook:9b06df75e445


