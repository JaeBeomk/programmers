from django.shortcuts import render,redirect
from posts.models import Post


# Create your views here.
def feeds(request):
    # request의 요청의 정보를 가져온다
    # user= request.user
    # 로그인 여부 확인
    # is_authenticated=user.is_authenticated
    # 검증
    # print("user:",user)
    # print("is_authenticated:",is_authenticated)

    # 로그인 여부 확인 후 로그인페이지로
    if not request.user.is_authenticated:
        return redirect("/users/login/")
    
    # 모든 글 목록을 템플릿으로 전달
    posts=Post.objects.all()
    context={"posts":posts}
    
    
    return render(request,"posts/feeds.html",context)