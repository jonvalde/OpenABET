from django.urls import path, include

from . import views 

urlpatterns = [
    path('', views.index, name='universities'),
    path('<int:university_id>', views.profilePage, name='university'),
]