from django.shortcuts import render, redirect
from .models import Task
from users.models import user
from django.contrib import messages
import requests
from django.contrib.auth import get_user_model
def home(request):
    return render(request, 'home.html')

def task_create(request):
    users = get_user_model().objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        assignee = user.objects.get(id=request.POST.get('assignee'))
        try:
            task = Task.objects.create(
                title=title,
                description=description,
                due_date=due_date,
                priority=priority,
                assignee=assignee
            )
            task.save()
            messages.success(request, 'Task created successfully')
            return redirect('task_list')
        except:
            messages.error(request, 'An error occurred while creating the task')
            return render(request, 'createTask.html', {'users': users})
    return render(request, 'createTask.html', {'users': users})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'viewTasks.html', {'tasks': tasks})
def task_update(request, id):
    users = get_user_model().objects.all()
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        assignee = user.objects.get(id=request.POST.get('assignee'))
        file = request.POST.get('file')
        try:
            task.title = title
            task.description = description
            task.due_date = due_date
            task.priority = priority
            task.assignee = assignee
            task.file = file
            task.save()
            messages.success(request, 'Task updated successfully')
            return redirect('task_list')
        except:
            messages.error(request, 'An error occurred while updating the task')

        return render(request, 'viewTasks.html', {'task': task})
    return render(request, 'updateTask.html', {'task': task, 'users': users})

def task_delete(request, id):
    task = Task.objects.get(id=id)
    try:
        task.delete()
        messages.success(request, 'Task deleted successfully')
        return redirect('task_list')
    except:
        messages.error(request, 'An error occurred while deleting the task')

    return render(request, 'viewTasks.html', {'task': task})

def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    redirect('viewTask')
    return render(request, 'completeTask.html', {'task': task})

def incomplete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = False
    task.save()
    redirect('viewTask')
    return render(request, 'incompleteTask.html', {'task': task})
def task_detail(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'taskDetail.html', {'task': task})