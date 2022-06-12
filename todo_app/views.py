from multiprocessing import context
from django.shortcuts import redirect, render
from . models import *

# Create your views here.


def home(request):

    context = {'todo_data':Data.objects.all()}
    if request.method == 'POST':
        v_data = request.POST.get('data')
        if v_data != ' ':
            Data.objects.create(data=v_data)

    return render(request,'todo_app/home.html',context)

def edit(request,id):

    context = {'todo_data':Data.objects.get(id=id)}

    if request.method == 'POST':
        v_data = request.POST.get('data')
        if v_data != ' ':
            Data.objects.filter(id=id).update(data=v_data)
        return redirect('/')
    return render(request,'todo_app/edit.html',context)    


def delete(request,pk):
    context = Data.objects.get(id=pk)
    context.delete()
    return redirect('/')


