from django.shortcuts import render, redirect
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def todolist(request):

    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Task Added!"))
        return redirect("todolist")
    else:
        # for the paginator
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 10)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)


        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect("todolist")

def edit_task(request,task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()

        messages.success(request, ("Task Edited!"))
        return redirect("todolist")
    else:

        task_obj = TaskList.objects.get(pk=task_id)

        return render(request, 'edit.html', {'task_obj': task_obj})

def complete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect("todolist")

def pending_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect("todolist")



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
