from django.urls import path

from . import views
from .views import *

app_name='main'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.index, name='index'),
    
    path('blog/',blog, name='blog'),
    
    # URL:80/blog/숫자로 접근시 게시글-세부 페이지
    path('blog/<int:pk>',posting,name="posting"),
]
