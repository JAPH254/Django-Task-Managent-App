from django.shortcuts import render, redirect
from .models import Task
from users.models import user
def home(request):
    return render(request, 'home.html')

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        assignee = user.objects.get(id=request.POST.get('assignee'))
        dependencies = request.POST.getlist('dependencies')
        task = Task(title=title, description=description, due_date=due_date, priority=priority, assignee=assignee)
        task.save()
        task.dependencies.set(dependencies)
        redirect('viewTask')

        userdata = user.objects.all()
        return render(request, 'createTask.html', {'userdata': userdata})
        
    return render(request, 'createTask.html')
 

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'viewTasks.html', {'tasks': tasks})

def task_update(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        assignee = user.objects.get(id=request.POST.get('assignee'))
        dependencies = request.POST.getlist('dependencies')
        task.title = title
        task.description = description
        task.due_date = due_date
        task.priority = priority
        task.assignee = assignee
        task.dependencies.set(dependencies)
        task.save()
        redirect('task_list')
        return render(request, 'updateTask.html', {'task': task})
    return render(request, 'updateTask.html', {'task': task})

def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    redirect('task_list')
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