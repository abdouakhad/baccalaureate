from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users

# Create your views here.


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Vous etes maintenant connecte")
            return redirect('dashboard')
        else:
            messages.info(
                request, "il ya une erreur sur le nom d'utilisateur ou le mot de passe")
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Vous etes maintenant deconnecte')
    return redirect('index')


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Ce nom d'utilisateur est deja pris")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Cet email a été deja utilisé')
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, password=password1, username=username)
            messages.success(request, 'Vous etes maintenant inscrit.')
            group = Group.objects.get(name='client')
            user.groups.add(group)
            return redirect('index')
        else:
            messages.error(request, 'Les mots de passe ne se ressemblent pas')
            return redirect('register')

    return render(request, 'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
