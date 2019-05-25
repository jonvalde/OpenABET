from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='professors'),
    path('<int:professor_id>', views.profilePage, name='professor'),
]