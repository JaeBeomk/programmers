from django.db import models

# Create your models here.

# 게시글(POST) 모델은 제목 내용이 필요
class Post(models.Model):
    postname=models.CharField(max_length=50)
    contents=models.TextField()
    # DB migrate 필요!
    # python manage.py makemigrations
    # python manage.py migrate
    mainphoto=models.ImageField(blank=True,null=True)
    # 게시글 Post에 이미지 추가
    # 모델 수정 후 사진 처리 라이브러리 Pillow 설치


    # 게시글의 제목이 Post Object 대신하기
    def __str__(self):
        return self.postname