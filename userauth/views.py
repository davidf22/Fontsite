from django.shortcuts import render, redirect
from django.contrib import messages
from userauth import forms as userauth_forms
from django.contrib.auth import authenticate, login, logout
from userauth import models as userauth_models
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def register_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in')
        return redirect('/')
    
    if request.method == 'POST':
        form = userauth_forms.UserRegistrationForm(request.POST or None)

        if form.is_valid():
            user = form.save()
            user_name = form.cleaned_data.get('first_name')
            if user is not None:
                messages.success(request, 'Account created successfully!')

                text_data = {
                    'user': user_name
                }
                # Send email after registration success
                subject = 'Testing welcome to Fontsite!'
                text_body = render_to_string('email/account_created.txt', text_data)
                html_body = render_to_string('email/account_created.html', text_data)
                msg = EmailMultiAlternatives(
                    subject=subject,
                    from_email=settings.FROM_EMAIL,
                    to=[user.email],
                    body=text_body
                )
                msg.attach_alternative(html_body, 'text/html')
                msg.send()
                
                return redirect("userauth:login")
            else:
                messages.error(request, 'Authentication failed. Please try logging in manually')
    else:
        form = userauth_forms.UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'auth/sign-up.html', context)


def login_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in')
        return redirect('/')

    form = userauth_forms.LoginForm()

    if request.method == 'POST':
        form = userauth_forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            phone_number = form.cleaned_data.get('phoneNumber')
            
            user = authenticate(request, email=email, password=password, phone_number=phone_number)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successfully')
                next_url = request.GET.get('next', '/')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid email or password')
        
    context = {
        'form': form
    }
    return render(request, 'auth/login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successfull')

    return redirect('userauth:login')