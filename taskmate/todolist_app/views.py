from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todolist(request):
    context = {

    }
    return render(request, 'todolist.html', context)

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
