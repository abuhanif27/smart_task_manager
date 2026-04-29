from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# views.py


def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        
        task = Task.objects.create(title=title)

        html = render_to_string("tasks/partials/task_item.html", {"task": task})

        return HttpResponse(html)
    

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponse("")

def edit_task(request, id):
    task = Task.objects.get(id=id)
    html = render_to_string("tasks/partials/task_edit.html", {"task": task})
    return HttpResponse(html)

def update_task(request, id):
    task = Task.objects.get(id=id)
    task.title = request.POST.get("title")
    task.save()

    html = render_to_string("tasks/partials/task_item.html", {"task": task})
    return HttpResponse(html)