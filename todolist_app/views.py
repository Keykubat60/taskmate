from django.shortcuts import render, redirect
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required()
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():

            # this code will save first the user manage name and then overwrite task
            # at the end it will save to the model
            instance = form.save(commit = False)
            instance.manage = request.user
            instance.save()

        messages.success(request, ("New Task Added!"))
        return redirect("todolist")
    else:
        # for the paginator
        all_tasks = TaskList.objects.filter(manage = request.user)
        paginator = Paginator(all_tasks, 50)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {'all_tasks': all_tasks})


@login_required()
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
         task.delete()
    else:
        messages.error(request, ("Access Restriced, You Are Not Allowed!"))

    return redirect("todolist")


@login_required()
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()

        messages.success(request, ("Task Edited!"))
        return redirect("todolist")
    else:

        task_obj = TaskList.objects.get(pk=task_id)

        return render(request, 'edit.html', {'task_obj': task_obj})


@login_required()
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("Access Restriced, You Are Not Allowed!"))

    return redirect("todolist")

@login_required()
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, ("Access Restriced, You Are Not Allowed!"))
    return redirect("todolist")


def index(request):
    """
    1. rendert ein HTML datei als Antwort zur??ck
    2. Ein inhalt{} wird immer erstellt auch wenn es leer sein sollte

    """
    context = {
        'index_text': "Welcome to Home Page.",

    }
    return render(request, 'index.html', context)


def contact(request):
    """
    1. rendert ein HTML datei als Antwort zur??ck
    2. Ein inhalt{} wird immer erstellt auch wenn es leer sein sollte

    """
    context = {
        'contact': "Welcome to Contact Page.",

    }
    return render(request, 'contact.html', context)


def about(request):
    """
    1. rendert ein HTML datei als Antwort zur??ck
    2. Ein inhalt{} wird immer erstellt auch wenn es leer sein sollte

    """
    context = {
        'about': "Welcome to About Page.",

    }
    return render(request, 'about.html', context)
