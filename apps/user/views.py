from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

from apps.user.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        confirm_password =request.POST.get('conf_pass')
        if password == confirm_password and username and email:
            user = User(username=username, email=email, password=password)
            user.save()

            user = authenticate(request=request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('index', user.id) 
    return render(request, 'register/register.html', locals())

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'Пользователь с таким именем не существует.')
            return redirect('login')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # перенаправление на главную страницу
        else:
            messages.error(request, 'Неправильный пароль')
            return redirect('login')
    return render(request, 'register/login.html', locals())
