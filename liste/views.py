from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from liste.choices import regions, villes, departments
from .models import Liste
from pages.models import Grade
# Create your views here.


def feature(request):
    queryset_list = Grade.objects.order_by('-grades')

    # Searching by Student Number
    if 'numero' in request.GET:
        numero = request.GET['numero']
        if numero:
            queryset_list = queryset_list.filter(
                student__student_number=numero)

    # Searching by Jury Number
    if 'jury' in request.GET:
        jury = request.GET['jury']
        if jury:
            queryset_list = queryset_list.filter(
                jury__jury_number=jury)

    # Searching by School Name
    if 'school' in request.GET:
        school = request.GET['school']
        if school:
            queryset_list = queryset_list.filter(
                student__school__icontains=school)

    # Searching by region Name
    if 'region' in request.GET:
        region = request.GET['region']
        if region:
            queryset_list = queryset_list.filter(
                student__region__iexact=region)

    # Searching by town Name
    if 'ville' in request.GET:
        ville = request.GET['ville']
        if ville:
            queryset_list = queryset_list.filter(
                student__ville__iexact=ville)

    # Searching by department Name
    if 'department' in request.GET:
        department = request.GET['department']
        if department:
            queryset_list = queryset_list.filter(
                student__department__iexact=department)

    paginator = Paginator(queryset_list, 5)  # Show 3 grades per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'regions': regions,
        'villes': villes,
        'departments': departments,
        'grades': page_obj,
        'values': request.GET
    }
    return render(request, 'features/feature.html', context)
