from django.contrib import admin
# from django.contrib.admin.widgets import AdminFileWidget
# from django.db import models
# from django.utils.safestring import mark_safe
from posts.models import Post,PostImage,Comment
# pip install 'django-admin-thumbnails<0.3' 명령어를 사용해 thumbnails 설치
import admin_thumbnails
# Register your models here.

# FK 연결된 다른객체 확인 하려면 admin의 Inline사용
class CommentInline(admin.TabularInline):
    model=Comment
    extra=1
    
# AdminFileWideget은 관리자 페이지에서 파일선택 버튼을 보여줌
# class InlineImageWidget(AdminFileWidget):
#     def render(self,name,value,attrs=None,renderer=None):
#         html=super().render(name,value,attrs,renderer)
#         if value and getattr(value,"url",None):
#             html=mark_safe(f'<img src="{value.url}" heigth="150">')+html
#         return html
    
@admin_thumbnails.thumbnail("photo") # InlineImageWidget 클래스를 django lib로 해결
class PostImageInline(admin.TabularInline):
    model=PostImage
    extra=1
    # formfield_overrides={
    #     models.ImageField:{
    #         "widget":InlineImageWidget,
    #     }
    # }

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=[
        "id",
        "content",
    ]
    inlines=[
        CommentInline,
        PostImageInline,
    ]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display=[
        "id",
        "post",
        "photo",
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=[
        "id",
        "post",
        "content",
    ]



