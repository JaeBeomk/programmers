from django.urls import path
from django.contrib import path

from . import views
from .views import *
# 이미지 업로드
from django.conf.urls.static import static
from django.conf import settings

app_name='main'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.index, name='index'),
    
    path('blog/',blog, name='blog'),
    
    # URL:80/blog/숫자로 접근시 게시글-세부 페이지
    path('blog/<int:pk>',posting,name="posting"),
]

# 이미지 URL설정
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
