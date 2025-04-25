"""
URL configuration for fontsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views
from .views import CreateCheckoutSessionView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('search/', views.mock_search, name='search'),

    path("login/", views.user_login, name="login"),

    path('accounts/', include('allauth.urls')),

    path("", views.home, name='home'), 

    path("fontshall/", views.fontshall, name='fontshall'),

    path("about/", views.about, name='about'),

    path("emerald/", views.emerald, name='emerald'), 

    path("amberhall/", views.amberhall, name='amberhall'), 

    path("kingscourt/", views.kingscourt, name='kingscourt'), 

    path("singlerm/", views.singlerm, name='singlerm'), 

    path("deluxe/", views.deluxe, name='deluxe'), 

    path("doublerm/", views.doublerm, name='doublerm'), 

    path("master/", views.master, name='master'), 

    path("booking/", views.booking, name='booking'), 

    path("paymentcom/", views.paymentcom, name='paymentcom'), 

    path("create-checkout-session/", CreateCheckoutSessionView.as_view(),name='create-checkout-session')

    
]
