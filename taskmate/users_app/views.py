from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):

    if request.method == "POST":
        register_form = UserCreationForm(request)
        #register_form.save()
        messages.success(request,("SUCCESFUL you create an user account!"))
        return redirect("register")
    else:


        register_form = UserCreationForm()
    return render(request, "register.html", {"register_form": register_form})
