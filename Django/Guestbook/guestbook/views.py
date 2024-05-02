from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from guestbook.models import Guestbook

# Create your views here.
def index(request):
    Guestbooks={'Guestbooks':Guestbook.objects.all()}
    return render(request, 'list.html',Guestbooks)

def post(request):
    if request.method == "POST":
        name = request.POST['name']
        title = request.POST['title']
        contents = request.POST['content']
        # sequence 초기화 생성
        gb=Guestbook.objects.all()
        id=gb.last().pk +1

        Guestbooks = Guestbook(id=id,name=name, title=title, contents=contents)
        Guestbooks.save()
        return HttpResponseRedirect('/') # index로
    else:
        return render(request, 'post.html')
 