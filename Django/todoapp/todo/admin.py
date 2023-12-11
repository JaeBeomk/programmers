from django.contrib import admin
# Todo 모델 객체 불러오기
from .models import Todo
# Register your models here.

admin.site.register(Todo)
