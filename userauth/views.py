from django.shortcuts import render, redirect
from django.contrib import messages
from userauth import forms as userauth_forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


def register_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in')
        return redirect('/')
    
    form = userauth_forms.USerRegistrationForm(request.POST or None)
    
    if form.is_valid():
        user = form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user_ = authenticate(email=email, password=password)
        if user_ is not None:
            login(request, user_)

            messages.success(request, 'Account created successfully!')
            return redirect("login")
        else:
            messages.error(request, 'Authentication failed. Please try loggin in manually')

    context = {
        'form': form
    }

    return render(request, 'auth/sign-up.html', context)