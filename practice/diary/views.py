from django.shortcuts import render, redirect,get_object_or_404
from .models import Day 
from .forms import DayCreateForm
# Create your views here.

def index(request):
    context = {
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