from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    total_tasks = len(tasks)
    completed_tasks = 0
    remaining_tasks = 0
    pct = 0
    for task in tasks:
        if task.done:
            completed_tasks += 1
    remaining_tasks = total_tasks - completed_tasks
    if total_tasks > 0:
        pct = (completed_tasks / total_tasks) * 100
    return render(
        request, 
        'tarefas/home.html',
        {
            'tasks': tasks,
            'total': total_tasks,
            'completed': completed_tasks,
            'remaining': remaining_tasks,
            'pct': pct
        })

def add(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')