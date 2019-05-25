from django.shortcuts import render
from .models import Department

# Create your views here.
def index(request):
    departments = Department.objects.all()
    context = {'departments' : departments}
    return render(request, 'departments/index.html', context)

def profilePage(request, department_id):
    d = Department.objects.get(id = department_id)
    context = {'d' : d}
    return render(request, 'departments/department.html', context)