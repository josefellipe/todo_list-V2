from django.shortcuts import render, HttpResponse
from .forms import TaskForm

def home(request):
    form = TaskForm()

    context = {
        'form': form
    }

    return render(request, 'home.html', context)

