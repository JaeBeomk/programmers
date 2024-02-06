from django.urls import path
from django.contrib import admin
from main.views import index ,blog ,posting, new_post,remove_post

# 이미지 업로드
from django.conf.urls.static import static
from django.conf import settings

app_name='main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    
    path('blog/',blog, name='blog'),
    
    # URL:80/blog/숫자로 접근시 게시글-세부 페이지
    path('blog/<int:pk>',posting,name="posting"),
    
    path('blog/new_post/', new_post),

    path('blog/<int:pk>/remove/', remove_post),
]

# 이미지 URL설정
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
