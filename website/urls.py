from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('apply/', views.apply, name='apply'),
    # path('/signup', views.signUp, name='signUp'),
]