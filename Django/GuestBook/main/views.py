from django.shortcuts import render
# view에 model 가져오기
from .models import Post


# Create your views here.
# index page 설정
def index(request):
    return render(request,'main/index.html')

# blog.html을 요청하는 함수
def blog(request):
    # post를 가져와 post_list에 저장
    post_list=Post.objects.all()
    # blog.html을 열 때, 모든 post인 post_list도 가져오게 {'key':value}
    return render(request, 'main/blog.html',{'post_list':post_list})
