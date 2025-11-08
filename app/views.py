from django.shortcuts import render
from django.http import HttpRequest, HttpResponse



# Create your views here.

def create_task(request: HttpRequest) -> HttpResponse:
    if request.method =="GET":
        return render (request, 'create.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        print(name, description, priority)
        return HttpResponse("Task created successfully")
    

