from django.shortcuts import render, redirect
from .models import user
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
            context = {'error_message': error_message}
            return render(request, 'login.html', context)
    else:
        context = {}
    return render(request, 'login.html', context)
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('login')


def users_list(request):
    users = user.objects.all()
    return render(request, 'createTask.html', {'users': users})
