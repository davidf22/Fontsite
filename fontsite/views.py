from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse


stripe.api_key= settings.STRIPE_SECRET_KEY

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        mock_username = "admin"
        mock_password = "password123"

        if username == mock_username and password == mock_password:
            # Simulate a successful login by redirecting to homepage
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "login.html", {"error": "Invalid username or password."})

    return render(request, "login.html")


def home(request):
    return render(request, 'home.html')

def mock_search(request):
    return HttpResponse("Search processed! (mock)")

def about(request):
    return render(request, 'about.html')

def fontshall(request):
    return render(request, 'fontshall.html')

def emerald(request):
    return render(request, 'emerald.html')

def kingscourt(request):
    return render(request, 'kingscourt.html')


def singlerm(request):
    return render(request, 'singleRm.html')

def deluxe(request):
    return render(request, 'deluxe.html')

def amberhall(request):
    return render(request, 'amberhall.html')

def doublerm(request):
    return render(request, 'doubleRm.html')

def master(request):
    return render(request, 'master.html')

def booking(request):
    return render(request, 'booking.html')

def paymentcom(request):
    return render(request, 'paymentcom.html')

class CreateCheckoutSessionView(View):
    def post(self, requests, *args, **kwargs): 
        YOUR_DOMAIN = "http://127.0.0.1:8000"
   
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/paymentcom.html',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )

        return JsonResponse({checkout_session.url})
    




