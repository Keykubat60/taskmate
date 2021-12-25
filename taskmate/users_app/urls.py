from django.urls import path
from users_app import views

urlpatterns = [
    path('register', views.register, name='register'),
]