from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('toggle/<int:task_id>/', views.toggle, name='toggle'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
]