from django.shortcuts import render
from django.http import HttpResponse
from todolist_app.models import TaskList

# Create your views here.
def todolist(request):
    all_tasks = TaskList.objects.all

    return render(request, 'todolist.html', {'all_tasks': all_tasks})


def contact(request):
    """
    1. rendert ein HTML datei als Antwort zurück
    2. Ein inhalt{} wird immer erstellt auch wenn es leer sein sollte

    """
    context = {
        'contact': "Welcome to Contact Page.",

    }
    return render(request, 'contact.html',context)


def about(request):
    """
    1. rendert ein HTML datei als Antwort zurück
    2. Ein inhalt{} wird immer erstellt auch wenn es leer sein sollte

    """
    context = {
        'about': "Welcome to About Page.",

    }
    return render(request, 'about.html',context)
