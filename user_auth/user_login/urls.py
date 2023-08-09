from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signup/', views.login, name='login'),
    path('home/', views.home, name='home'),
]
    