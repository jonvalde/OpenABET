
from django.shortcuts import render
from .models import University

# Create your views here.
def index(request):
    universities = University.objects.all()
    context = {'all' : universities}
    return render(request, 'universities/index.html', context)

def profilePage(request, university_id):
    u = University.objects.get(id = university_id)
    context = {'u' : u}
    return render(request, 'universities/university.html', context)