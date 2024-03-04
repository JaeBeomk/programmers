from django.shortcuts import render, redirect
from blog.models import Post,Comment
# Create your views here.

def post_list(request):
    posts= Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request,"post_list.html",context)


# 상세페이지
def post_detail(request,post_id):
    post = Post.objects.get(id=post_id)
    # print(post)
    if request.method=="POST":
        # textarea의 name 속성값("comment")추출
        comment_content=request.POST["comment"]
        # print(comment_content)
        Comment.objects.create(
            post=post,
            content=comment_content,
        )
        # POST의 댓글 생성이나 GET의 상세페이지 보여주는 요청 둘다 상세페이지로 render
    context = {
        "post":post,
    }
    return render(request, "post_detail.html",context)

def post_add(request):
    if request.method == "POST":
        print(request.FILES)
        print("method POST")
        title= request.POST["title"]
        content = request.POST["content"]
        thumbnail= request.FILES["thumbnail"] # 이미지 파일
        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail,
        )
        # 객체 생성시 post로 보내기
        return redirect(f"/posts/{post.id}/")
    else:
        print("method GET")
        return render(request, "post_add.html")