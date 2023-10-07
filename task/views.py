from django.shortcuts import render, redirect,HttpResponse
from .forms import TaskForm
from .models import Task


def home(request):
    tasks               = Task.objects.all()
    tasks_todo          = Task.objects.filter(status='todo')
    tasks_in_progress   = Task.objects.filter(status='in_progress')
    tasks_is_complete   = Task.objects.filter(status='is_complete')

    form_add = TaskForm()
    form = [(0,form_add)]
    for task in tasks:
        form.append((task.pk,TaskForm(instance=task)))

    context = {
        'form': form,
        'all_tasks': tasks,
        'tasks_todo': tasks_todo,
        'tasks_in_progress': tasks_in_progress,
        'tasks_is_complete': tasks_is_complete
    }

    return render(request, 'home.html', context)


def add_task(request):
    Task.objects.create(
        owner       = request.POST['owner'],
        title       = request.POST['title'],
        description = request.POST['description'],
        status      = request.POST['status'],
        priority    = request.POST['priority']
    )

    return redirect('/task')


def delete_task(request, pk):

    task = Task.objects.get(pk=pk)
    task.delete()

    return redirect('/task')


def update_task(request, pk):

    task = Task.objects.get(pk=pk)
    
    task.owner       = request.POST['owner']
    task.title       = request.POST['title']
    task.description = request.POST['description']
    task.status      = request.POST['status']
    task.priority    = request.POST['priority']

    task.save()

    return redirect('/task')