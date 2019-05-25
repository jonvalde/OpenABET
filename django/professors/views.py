from django.shortcuts import render

from .models import Professor

# Create your views here.
def index(request):
    professors = Professor.objects.all()
    context = {'professors' : professors}
    return render(request, 'professors/index.html', context)

def profilePage(request, professor_id):
    p = Professor.objects.get(id = professor_id)
    context = {'p' : p}
    return render(request, 'professors/professor.html', context)