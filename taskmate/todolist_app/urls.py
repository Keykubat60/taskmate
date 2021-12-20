from todolist_app import views
from django.urls import path

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('delete/<task_id>',views.delete_task,name='delete_task'),
]
