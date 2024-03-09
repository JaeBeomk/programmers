from django.shortcuts import render,redirect
from users.forms import LoginForm,SignupForm
from users.models import User
from django.contrib.auth import authenticate,login,logout

# login 로직
def login_view(request):
    # login 완료 상태시
    if request.user.is_authenticated:
        return redirect("posts:feeds")
    
    if request.method=="POST":
        # LoginForm인스턴스 사용
        form = LoginForm(data=request.POST)
        
        # 데이터 유효셩검사
        # print("form.is_valid():",form.is_valid())
        # 데이터가 유효하다면
        if form.is_valid():
            # 유효성 검사 이후 cleaned_data에서 데이터 가져와 사용
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]

            # 해당 사용자가 있는지 체크
            user=authenticate(username=username,password=password)

            # 사용자 존재시
            if user:
                # 로그인 처리 후 피드로 redirect
                login(request,user)
                return redirect("posts:feeds")
            else:
                # print("로그인 실패")
                form.add_error(None,"입력한 ID의 해당 사용자가 없습니다.")

        # 생성된 인서턴스를 템플릿에 form 키로 전달
        # 실패한 경우 다시 LoginForm으로 렌더링
        context={"form":form}
        return render(request,"users/login.html",context)

    else:
        form =LoginForm()
        context={"form":form}
        return render(request,"users/login.html",context)

# logout 로직 
def logout_view(request):
    logout(request)
    return redirect("users:login")

def signup(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            # 회원가입에 관련한 내용을 모두 form에서 처리
            
            user= form.save()
            login(request,user)
            return redirect("posts:feeds")
    # 중복된 코드는 최적화
    else:
        form=SignupForm()
    context={"form": form}
    return render(request,"users/signup.html",context)