from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root path
    path('members/', views.members, name='members'),
]