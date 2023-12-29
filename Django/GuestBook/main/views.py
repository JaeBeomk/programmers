from django.shortcuts import render

# Create your views here.
# index page 설정
def index(request):
    return render(request,'main/index.html')
