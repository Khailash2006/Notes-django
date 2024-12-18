from django.shortcuts import render,HttpResponse,redirect
from .models import todo
from .form import Listform

# Create your views here.
def home(request):
    title = todo.objects.all()
    return render(request,'home.html',{'title':title})

def add(request):
    if request.method == 'POST':
        newform = Listform(request.POST)
        if newform.is_valid():
            newform.save()
            return HttpResponse("New notes added")
        else:
            print(newform.errors)
            return render(request,'add.html',{'form':newform})
    else:
        newform = Listform()

    return render(request,'add.html',{'form':newform})

def display(request,num):
    title = todo.objects.get(id = num)
    return render(request,'display.html',{'title':title})

def update(request,num):
    title = todo.objects.get(id = num)
    newform = Listform(request.POST,instance=title)
    if request.method == 'POST':
        if newform.is_valid():
           newform.save()
           return HttpResponse("New value updated")
        else:
            return HttpResponse("New value is not updated")
    else:
        return render(request,'update.html',{'form':newform})
    
def delete(request,num):
    dele = todo.objects.get(id = num)
    if request.method == 'POST':
        dele.delete()
        return redirect('home')
    else:
        return render(request,'delete.html')