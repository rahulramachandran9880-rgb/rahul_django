from django.conf.locale import fr
from django.shortcuts import render,redirect
from django.template.backends import django
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin,logout as authlogout
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    error_message = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user :
            authlogin(request, user)
            return redirect('list')
            print(user)
        else:
            error_message = "Invalid username or password"
    return render(request, 'users/login.html', {'error_message': error_message})

def logout(request):
    authlogout(request)     
    return redirect('login')

def signup(request):
    user = None
    error_message = None
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except Exception as e:
            error_message = str(e)
    return render(request, 'users/create.html',{ 'user': user ,'error_message': error_message })