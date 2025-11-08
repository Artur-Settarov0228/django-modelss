from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Task



# Create your views here.

def create_task(request: HttpRequest) -> HttpResponse:
    if request.method =="GET":
        return render (request, 'create.html')
    else :
        form= request.POST
        new_task = Task(

        name = form.get('name'),
        description = form.get('description'),
        priority = form.get('priority')
    )
        new_task.save()
        return HttpResponse(f"Task created with id: {new_task.id}")
    

def task_list (request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    return render (request, 'list.html', {'tasks': tasks})



      

