from django.shortcuts import render, redirect,get_object_or_404
from .models import Day, Comment
from .forms import DayCreateForm,CommentCreateForm
# Create your views here.

def index(request):
    flg = set(Comment.objects.values_list('comment_id',flat=True))
    context = {
        'flg':flg,
        'day_list':Day.objects.all(),
    }
    return render(request,'diary/index.html',context)

def add(request):
    form = DayCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('diary:index')
    context = {
        'form':form
    }
    return render(request,'diary/add.html',context)

def edit(request,pk):
    day = get_object_or_404(Day,pk=pk)
    form = DayCreateForm(request.POST or None, instance=day)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')
    context = {
        'form':form
    }
    return render(request,'diary/add.html',context)

def delete(request,pk):
    day = get_object_or_404(Day,pk=pk)
    if request.method == 'POST':
        day.delete()
        return redirect('diary:index')
    context = {
        'day':day
    }
    return render(request,'diary/delete.html',context)

def detail(request,pk):
    day = get_object_or_404(Day,pk=pk)
    form = CommentCreateForm(request.POST or None,initial={'comment_id':day.id})
    print(form)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')
    comments = Comment.objects.filter(comment_id=day.id)
    context = {
        'day':day,
        'form':form,
        'comments':comments
    }
    return render(request,'diary/detail.html',context)