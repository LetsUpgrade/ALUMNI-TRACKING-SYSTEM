from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import User
# from .forms import AddAlumniForm
from django.views.generic import View
from .filters import AlumniFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    no_of_alumnis = User.objects.filter(is_college=False).filter(is_superuser=False).all().count()
    no_of_colleges = User.objects.filter(is_college=True).all().count()
    context = {
        "no_of_colleges":no_of_colleges,
        "no_of_alumnis":no_of_alumnis
    }
    return render(request, 'home.html',context)


def AlumniListView(request):
    total = User.objects.filter(Verified=True).filter(is_college=False).all()
    alfilter = AlumniFilter(request.GET, queryset=total)
    template_name = 'showalumni.html'
    paginator = Paginator(alfilter.qs, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, template_name, {'filter': alfilter, 'page_obj': page_obj})


def CollegeListView(request):
    total = User.objects.filter(is_college=True).all()
    template_name = 'showcollege.html'
    paginator = Paginator(total, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, template_name, {'filter': total, 'page_obj': page_obj})


class CollegeDetailView(View):
    def get(self, request, *args, **kwargs):
        college = get_object_or_404(User, pk=kwargs['pk'])
        alumnis = User.objects.filter(is_college=False).filter(College=college.College).filter(Verified=True).all()
        context = {'college': college,'alumnis':alumnis}
        return render(request, "college.html", context)


class AlumniDetailView(View):
    def get(self, request, *args, **kwargs):
        alumni = get_object_or_404(User, pk=kwargs['pk'])
        context = {'alumni': alumni}
        return render(request, "alumni.html", context)
