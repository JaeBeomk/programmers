from django.shortcuts import render,redirect
from posts.models import Post,Comment,PostImage,HashTag
from posts.forms import CommentForm,PostForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse

# 게시글 list
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
        return redirect("users:login")
    
    # 모든 글 목록을 템플릿으로 전달
    posts=Post.objects.all()
    comment_form=CommentForm()
    context={
        "posts":posts,
        "commnet_form":comment_form,
        }
    
    return render(request,"posts/feeds.html",context)

# 댓글 작성을 처리할 View, POST 요청만 허용
@require_POST 
def comment_add(request):
    # print(request.POST)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # commit=False 옵션으로 메모리상 comment 객체 생성
        comment = form.save(commit=False)

        # Comment 생성에 필요한 사용자 정보를 request에서 가져와 할당
        comment.user = request.user

        # DB에 Comment 객체 저장
        comment.save()
        # comment의 정보 확인
        # print(comment.id)
        # print(comment.content)
        # print(comment.user)
        
        # URL로 next값을 전달 받았다면 댓글 작성 완료 후 전달받은 값으로 이동
        if request.GET.get("next"):
            url_next=request.GET.get("next")
        
        else:
            url_next=reverse("posts:feeds")+ f"#post-{comment.post.id}"
        return HttpResponseRedirect(url_next)        
        
        # 생성 완료 후에는 피드 페이지로 다시 이동
        # return HttpResponseRedirect(f"/posts/feeds/#post-{comment.post.id}")
        # url=reverse("posts:feeds") + f"#post-{comment.post.id}"
        # return HttpResponseRedirect(url)

# 댓글삭제
@require_POST
def comment_delete(request, comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        if comment.user== request.user:
            comment.delete()
            url=reverse("posts:feeds") + f"#post-{comment.post.id}"
            return HttpResponseRedirect(url)
        else:
            return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다.")
            
# 게시글 생성
def post_add(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()

            for image_file in request.FILES.getlist("iamges"):
                PostImage.objects.create(
                    post=post,
                    photo=image_file,
                )
            tag_string= request.POST.get("tags")
            if tag_string:
                tag_names = [tag_name.strip() for tag_name in tag_string.split(",")]
                for tag_name in tag_names:
                    tag, _=HashTag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)
            url=reverse("posts:feeds")+f"#post-{post.id}"
            return HttpResponseRedirect(url)
    else:
        form=PostForm()
    context={"form":form}
    return render(request,"posts/post_add.html",context)

# tag
def tags(request,tag_name):
    try:
        tag = HashTag.objects.get(name=tag_name)
    except HashTag.DoesNotExist:
        posts = Post.objects.none()        
    else:
        posts=Post.objects.filter(tags=tag)
    context={
        "tag_name":tag_name,
        "posts":posts,
    }
    return render(request,'posts/tags.html',context)

# 게시글 상세
def post_detail(request, post_id):
    post=Post.objects.get(id=post_id)
    comment_form=CommentForm()
    context={"post":post,"comment_form":comment_form,}
    return render(request, "posts/post_detail.html",context)

# 좋아요
def post_like(request, post_id):
    post=Post.objects.get(id=post_id)
    user=request.user

    # 사용자가 좋아요 누를 Post목록에 좋아요 버튼을 누를 Post가 존재시 삭제
    if user.like_posts.filter(id=post.id).exists():
        user.like_posts.remove(post)

    else:
        user.like_posts.add(post)

    url_next=request.GET.get("next") or reverse("posts:feeds")+f"#post-{post.id}"
    return HttpResponseRedirect(url_next)