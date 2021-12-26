from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("REGISTRATION SUCCESS!"))
            return redirect("register")
        else:
            messages.error(request, (register_form.error_messages.keys()))
            return redirect("register")
    else:

        register_form = CustomRegisterForm()
    return render(request, "register.html", {"register_form": register_form})
