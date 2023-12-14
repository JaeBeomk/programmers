from django.shortcuts import render
from . import models

# Create your views here.
# todo/todo_list.html을 연결
# 완료되지않은 todo만 필터링 후 todos변수에 담아 전달
def todo_list(request):
    todos= Todo.object.filter(completed=False)
    return render(request,'todo/todo_list.html',{'todos':todos})

# todo/todo_detail.html 연결시킬 view생성
def todo_detail(request,pk):
    todo= Todo.objects.get(id=pk)
    return render(request,'todo/todo_detail.html',{'todo':todo})

# 생성작업
def todo_post(request):
    if  request.method=="POST":
        form= TodoForm(request.POST)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request,'todo/todo_post.html',{'form':form})

# 수정과의 차이는 instance를 받아온다는것이다
def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_post.html', {'form': form})

# 완료시 completed 상태로 변경 로직
def todo_done(request,pk):
    todo=Todo.objects.get(id=pk)
    todo.completed=True
    todo.save()
    return redirect('todo_list')

def todo_done_list(request):
    dones= Todo.objects.filter(completed=True)
    return render(request,'todo/todo_done_list.html',{'dones':done})

    
     
    