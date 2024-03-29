from django.shortcuts import render
# view에 model 가져오기
from .models import Post

# 컨트롤러 역활

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

# blog의 게시글을 부르는 posting 함수
def posting(request,pk):
    # 게시글중 pk를 이용해 하나의 글을 검색
    post=Post.objects.get(pk=pk)
    # posting.html을 열때 찾은 게시글을 post명칭의 값으로 가져옴
    return render(request, 'main/posting.html',{'post':post})

# 글쓰기 페이지 연동
def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})