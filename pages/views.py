from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from accounts.decorators import unauthenticated_user, allowed_users


# @allowed_users(allowed_roles=['client'])
def index(request):
    return render(request, 'pages/index.html')


# @allowed_users(allowed_roles=['client'])
def about(request):
    return render(request, 'pages/about.html')
