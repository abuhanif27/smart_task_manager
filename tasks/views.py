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