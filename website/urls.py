from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact_us.html', views.contact, name="contact"),
    path('appointment.html', views.appointment, name="appointment")
]