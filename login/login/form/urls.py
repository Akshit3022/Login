# this file is created by Akshit

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.register, name='register'),
    path('home', views.home, name='home'),
    path('add', views.add, name='add'),
    path('edit', views.edit, name='edit'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('logout', views.logout, name='logout'),
]
