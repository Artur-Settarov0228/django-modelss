import base64
import json

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse 
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
    
    context = {
        'tasks': tasks
    }
    return render (request= request, context=context, template_name='list.html')


def counter_view(request: HttpRequest) -> HttpResponse:

    bady = request.body.decode()

    data = json.loads(bady)
    print(data['name'], data['age'])

    return HttpResponse("Data received")


def get_user(requset:HttpRequest, slug: str) -> HttpResponse:
    text = "Hello, this is a, sample user data."
    slug = sulgify(text)


    data= [
        {
        "name": "John Doe",
        "price" : 29.99,
        "slug_name": "samsung-galaxy-s21",
        "id" : 1
        }
    ]
    requset = JsonResponse(data=data, safe=False, header={'Custom-Header': 'CustomValue'}, status=200)
    return requset
    
    
        

    
















      

