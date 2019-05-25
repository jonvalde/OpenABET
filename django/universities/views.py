
from django.shortcuts import render
from .models import University
from campuses.models import Campus

# Create your views here.
def index(request):
    universities = University.objects.all()
    context = {'all' : universities}
    return render(request, 'universities/index.html', context)

def profilePage(request, university_id):
    u = University.objects.get(id = university_id)
    cs = Campus.objects.filter(university_id = university_id)
    context = {
        'u' : u, 
        'cs' : cs,
    }
    return render(request, 'universities/university.html', context)