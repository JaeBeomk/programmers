# 방명록 프로젝트
- config 프로젝트 생성 후 templates dir 연동(config/settings.py)
- guestbook app 생성 후 apps 연동(config/settings.py)
- templates-> index.html 생성
- config/views.py 생성 후 index.html 컨트롤러 연동(views.py)
- urls.py에 config/views.py의 index 연동(config/urls.py)
- python manage.py runserver -> web서버 기동 후 확인
- superuser 생성
- 방명록에 대한 모델 정의(config/models.py)
- guestbook/admin 에 model 등록 (DB 마이그레이션)
- bootstrap에서 css/js 추가
(https://getbootstrap.com/docs/4.5/getting-started/download/)
- config/settings.py에 static폴더 연동
- list.html 생성 후 config/views.py index변경
- post.html 생성 후 config/views.py 연동 및 config/urls.py 연동
- 동작 확인
- sequence 방어문 생성 추후 다시 생성 예정(guestbook.views.py)

