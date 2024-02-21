# django 에서 view는 스프링의 컨트롤러 역활
from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger

# 컨트롤러(view) 와 뷰(urls)를 연동
def main(request):
    # 여기서 HttpResponse 는 장고가 돌려준 값을 브라우저가 읽을수있게 처리
    # return HttpResponse("안녕하슈?")
    # render의 첫arg는 view 함수에 전달되는 request객체로 지정 두번재arg는 경로
    return render(request,"main.html") 

# 리스트 페이지 연동
# burger_list 오브젝트 가져오는 내용 추가
def burger_list(request):
    burgers=Burger.objects.all()
    print("전체 햄버거 목록:",burgers) # 여기서 print는 localhost:8000/burgers/ 호출시 터미널에 출력됨

    # Template으로 전달해줄 객체
    context ={
        "burgers":burgers,  # burgers 키 값에 burgers 변수(QuerySet) 객체 value값으로 전달
    }
    # render 함수에 context 값 전달
    return render(request , "burger_list.html",context)
    
# 특정 버거 검색을 위한 view
def burger_search(request):
    # print(request.GET) # get방식으로 url상에 데이트값을 가져옴 test
    # request.GET에서 "keyword"의 키값을 가져와 출력
    keyword = request.GET.get("keyword")
    print(keyword)

    # 이름에 전달받은 키워드 값이 포함된 burger를 검색
    # keyword 값이 dict에 없을경우 에러가 발생하므로 방어문 추가
    if keyword is not None:
        burgers=Burger.objects.filter(name__contains=keyword)
        print(burgers)
    else:
        # 값이 없으면 빈 QuerySet할당
        burgers=Burger.objects.none()

    # 검색한 버거를 Template에 보여주기
    context = {
        "burgers": burgers,
    }
    return render(request,"burger_search.html",context)

