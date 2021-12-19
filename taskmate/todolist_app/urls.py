from todolist_app import views
from django.urls import path

urlpatterns = [
    path('', views.todolist, name='todolist'),

]
