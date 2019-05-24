from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='campuses'),
    path('<int:campus_id>', views.profilePage, name='campus'),
]
