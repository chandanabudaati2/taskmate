from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages

def register(request):
    if request.method=="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New User Account Created, Login To Get Started!")
            return redirect('login')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})

#def logout_view(request):
    logout(request)
    #messages.info(request, "Logged Out of Taskmate, Thank You For Using Us!")
    return redirect('login')
