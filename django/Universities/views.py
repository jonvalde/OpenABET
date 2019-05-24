from django.shortcuts import render
from .models import University

# Create your views here.
def index(request):
    Universities = University.objects.all()
    context = {'all' : Universities}
    return render(request, 'Universities/index.html', context)

def profilePage(request, University_id):
    U = University.objects.get(id = University_id)
    context = {'u' : U}
    return render(request, 'Universities/University.html', context)