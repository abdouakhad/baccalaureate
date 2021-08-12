from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        my_id = request.POST['my_id']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if int(my_id) != 123456789:
                print(my_id)
                messages.error(
                    request, "Votre numero d'identite jury est incorrecte.")
                return redirect('login_admin')
            auth.login(request, user)
            messages.success(request, "Vous etes maintenant connecte")
            return redirect('dashboard_jury')
        else:
            messages.info(
                request, "il ya une erreur sur le nom d'utilisateur ou le mot de passe")
            return redirect('login')
    return render(request, 'jury/login_jury.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Vous etes maintenant deconnecte')
    return redirect('index')


def register_admin(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        my_id = request.POST['my_id']
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Ce nom d'utilisateur est deja pris")
                return redirect('register')
            if int(my_id) != 123456789:
                print(my_id)
                messages.error(
                    request, "Votre numero d'identite jury est incorrecte.")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Cet email a été deja utilisé')
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, password=password1, username=username)
            messages.success(request, 'Vous etes maintenant inscrit.')
            group = Group.objects.get(name='jury')
            user.groups.add(group)
            return redirect('dashboard_jury')
        else:
            messages.error(request, 'Les mots de passe ne se ressemblent pas')
            return redirect('register')

    return render(request, 'jury/register_jury.html')


def logout_admin(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Vous etes maintenant deconnecte')
    return redirect('login_admin')


def dashboard_jury(request):
    return render(request, 'jury/dashboard_jury.html')
