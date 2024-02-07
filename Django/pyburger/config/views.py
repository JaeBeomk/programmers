# django 에서 view는 스프링의 컨트롤러 역활
from django.http import HttpResponse
from django.shortcuts import render
# 컨트롤러(view) 와 뷰(urls)를 연동
def main(request):
    # 여기서 HttpResponse 는 장고가 돌려준 값을 브라우저가 읽을수있게 처리
    # return HttpResponse("안녕하슈?")
    # render의 첫arg는 view 함수에 전달되는 request객체로 지정 두번재arg는 경로
    return render(request,"main.html") 

# 리스트 페이지 연동
def burger_list(request):
    # return HttpResponse("list 표시")
    return render(request , "burger_list.html")
    
