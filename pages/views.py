from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.

from accounts.decorators import unauthenticated_user, allowed_users
from pages.models import Grade

# @allowed_users(allowed_roles=['client'])


def index(request):
    grades = Grade.objects.order_by('-grades')
    # grades = Grade.objects.order_by('-grades').filter(grades__gte=10)

    context = {
        'grades': grades
    }
    return render(request, 'pages/index.html', context)


# @allowed_users(allowed_roles=['client'])
def about(request):
    return render(request, 'pages/about.html')
