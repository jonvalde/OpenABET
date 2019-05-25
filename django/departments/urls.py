from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='departments'),
    path('<int:department_id>', views.profilePage, name='department'),
]