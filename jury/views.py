from liste.models import Liste
from pages.models import Grade
from .forms import GradeForm
from accounts.decorators import unauthenticated_user, unauthenticated_user2, allowed_users
from .models import Jury
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages, auth
from django.core.paginator import Paginator


@unauthenticated_user2
def login_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        my_id = request.POST['my_id']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if int(my_id) != 1234:
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
            return redirect('login_admin')
    return render(request, 'jury/login_jury.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Vous etes maintenant deconnecte')
    return redirect('index')


@unauthenticated_user2
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
                return redirect('register_admin')
            if int(my_id) != 1234:
                print(my_id)
                messages.error(
                    request, "Votre numero d'identite jury est incorrecte.")
                return redirect('register_admin')
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
            return redirect('register_admin')

    return render(request, 'jury/register_jury.html')


def logout_admin(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Vous etes maintenant deconnecte')
    return redirect('login_admin')


@login_required(login_url='login_admin')
@allowed_users(allowed_roles=['jury'])
def dashboard_jury(request):
    jury = Jury.objects.get(user=request.user)
    jury_number = jury.jury_number

    # Importing all our modelss
    grades = Grade.objects.filter(jury=jury_number)
    student = Liste.objects.filter(jury_number=jury_number)
    form = GradeForm()

    form.fields['student'].queryset = Liste.objects.filter(
        jury_number=jury_number, choosen=False)

    form.fields['jury'].queryset = Jury.objects.filter(
        jury_number=jury_number)

    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            print('Yes Form is Valid')
            the_student = Liste.objects.get(pk=form.instance.student.pk)
            print(the_student)
            the_student.choosen = True
            the_student.save()
            form.save()
            return redirect('dashboard_jury')

    # Counting the number of students that succeed
    admin = grades.filter(grades__gte=10).order_by('-created_date')
    display_grades = admin
    display_grades_rank = admin.order_by('-grades')
    paginator = Paginator(display_grades_rank, 5)  # Show 3 grades per page.
    page_number = request.GET.get('page')
    page_obj_rank = paginator.get_page(page_number)

    admin = admin.count()

    # Counting the overall number of student
    number_student = student.count()

    # Calculating the percentage
    if student == 0:
        percentage = 0
    else:
        percentage = admin/number_student * 100

    context = {
        'display_grades_rank': page_obj_rank,
        'form': form,
        'number_student': number_student,
        'jury_number': jury_number,
        'admin': admin,
        'percentage': percentage,
        'display_grades': display_grades,
    }
    return render(request, 'jury/dashboard_jury.html', context)
