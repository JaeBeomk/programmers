from django.urls import path
from . import views


urlpatterns = [
    # todo 앱에서 목록화면에대한 url설정
    path('',views.todo_list,name='todo_list'),
    
    # todo_detail에 경로 추가
    path('<int:pk>/',views.todo_detail,name='todo_detail'),
    
    # 생성/ 수정을 위한 url연결
    path('post/', views.todo_post, name='todo_post'),
    path('<int:pk>/edit/', views.todo_edit, name='todo_edit'),

    # 완료시 확인 연결
    path('done/', views.todo_done_list, name='todo_done_list'),
    path('done/<int:pk>', views.todo_done, name='todo_done')
]
