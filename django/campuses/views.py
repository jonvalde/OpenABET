from django.shortcuts import render
from .models import Campus

# Create your views here.
def index(request):
    campuses = Campus.objects.all()
    context = {'campuses' : campuses}
    return render(request, 'campuses/index.html', context)

def profilePage(request, campus_id):
    c = Campus.objects.get(id = campus_id)
    context = {'c' : c}
    return render(request, 'campuses/campus.html', context)