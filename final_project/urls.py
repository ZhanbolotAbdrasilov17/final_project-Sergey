from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('menu', menu, name="menu"),
    path('team', team, name="team"),
    path('service', service, name="service"),
    path('testimonial', testimonial, name="testimonial"),
    path('contact', contact, name="contact"),




]

