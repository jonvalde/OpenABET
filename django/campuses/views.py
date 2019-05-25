from django.shortcuts import render
from .models import Campus
from departments.models import Department

# Create your views here.
def index(request):
    campuses = Campus.objects.all()
    context = {'campuses' : campuses}
    return render(request, 'campuses/index.html', context)

def profilePage(request, campus_id):
    c = Campus.objects.get(id = campus_id)
    ds = Department.objects.filter(campus_id = campus_id)
    context = {
        'c' : c,
        'ds' : ds,
    }
    return render(request, 'campuses/campus.html', context)