from django.shortcuts import render
from .models import Department
from professors.models import Professor

# Create your views here.
def index(request):
    departments = Department.objects.all()
    context = {'departments' : departments}
    return render(request, 'departments/index.html', context)

def profilePage(request, department_id):
    d = Department.objects.get(id = department_id)
    ps = Professor.objects.filter(department_id = department_id)
    context = {
        'd' : d,
        'ps': ps,
    }
    return render(request, 'departments/department.html', context)