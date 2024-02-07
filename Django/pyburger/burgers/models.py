from django.db import models

# Create your models here.
# 햄버거 가게를 차린다면 이름 가격 칼로리 정도로 보고 시작
# MVC중 M인 model을 설계하자 dto를 설계한다고 이해해자
# 설계한 모델을 DB 테이블이되려면 migration이 필요하다 
class Burger(models.Model):
    name=models.CharField(max_length=20)    # 문자열 20
    price=models.IntegerField(default=0)    # 숫자열
    calories=models.IntegerField(default=0) # 숫자열
    
    # 관리자 페이지에서 데이터 정보를 더 정확히
    def __str__(self):
        return self.name
    

