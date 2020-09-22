from django.shortcuts import render, redirect
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