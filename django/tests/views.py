from django.shortcuts import render

# Create your views here.
from .models import Test

# Create your views here.
def index(request):
    tests = Test.objects.all()
    context = {'tests' : tests}
    return render(request, 'tests/index.html', context)

def profilePage(request, test_id):
    t = Test.objects.get(id = test_id)

    context = {'t' : t}
    return render(request, 'tests/tests.html', context)