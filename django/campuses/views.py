from django.shortcuts import render
from .models import Campus

# Create your views here.
def index(request):
    campus = Campus.objects.all()
    context = {'all' : campus}
    return render(request, 'campuses/index.html', context)

def profilePage(request, campus_id):
    C = Campus.objects.get(id = campus_id)
    context = {'c' : C}
    return render(request, 'campuses/campus.html', context)