from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='Universities'),
    path('<int:University_id>', views.profilePage, name='University'),
]
