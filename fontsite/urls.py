from django.contrib import admin
from django.urls import include, path
from . import views
from .views import CreateCheckoutSessionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('userauth.urls')),
    path('search/', views.mock_search, name='search'),
    # path('accounts/', include('allauth.urls')),
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
