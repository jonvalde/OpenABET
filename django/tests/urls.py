from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='tests'),
    path('<int:test_id>', views.profilePage, name='test'),
]