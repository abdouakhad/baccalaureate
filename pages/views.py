from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from accounts.decorators import unauthenticated_user, allowed_users
from pages.models import Grade

# @allowed_users(allowed_roles=['client'])


def index(request):
    grades = Grade.objects.order_by('-grades')
    # grades = Grade.objects.order_by('-grades').filter(grades__gte=10)

    grade_list = Grade.objects.order_by('-grades')
    paginator = Paginator(grade_list, 3)  # Show 3 grades per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        # 'grades': grades,
        'grades': page_obj
    }
    return render(request, 'pages/index.html', context)


# @allowed_users(allowed_roles=['client'])
def about(request):
    return render(request, 'pages/about.html')


def student_info(request, student_id):
    student_info = get_object_or_404(Grade, pk=student_id)
    context = {
        'grade': student_info,
    }
    return render(request, 'info/student.html', context)
