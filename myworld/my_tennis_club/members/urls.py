from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),  # now the root URL will display "Hello, World"
]