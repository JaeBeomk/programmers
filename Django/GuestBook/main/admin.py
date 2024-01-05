from django.contrib import admin
from .models import Post
# Register your models here.

# admin에게 게시글 접근권한 생성
admin.site.register(Post)