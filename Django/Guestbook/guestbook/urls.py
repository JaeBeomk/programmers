from django.urls import path

from guestbook.views import index,post

urlpatterns = [
    path('',index,name='index'),
    path('/',index,name='index'),
    path('post',post,name='post'),
    path('post/',post,name='post'),
    
]

