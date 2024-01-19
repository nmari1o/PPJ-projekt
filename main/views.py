from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from main.models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
## Create your views here.

def all_tasks(request):
    tasks = Task.objects.all()
    grouped_tasks = {}
    for task in tasks:
        category = task.category
        if category in grouped_tasks:
            grouped_tasks[category].append(task)
        else:
            grouped_tasks[category] = [task]

    return render(request, 'all_tasks.html', {'grouped_tasks': grouped_tasks})

    
def tasks_by_category(request, category):
    tasks=Task.objects.filter(category=category)
    return render(request, 'tasks_by_category.html', {'tasks':tasks, 'category':category})    


def task_input(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:all_tasks')  
    else:
        form = TaskForm()

    return render(request, 'task_input.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('main:all_tasks')

def task_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('main:all_tasks')



