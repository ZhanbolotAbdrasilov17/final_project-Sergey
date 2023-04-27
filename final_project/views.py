from django.shortcuts import render
from django.urls import path
from django.conf import settings
from django.http import HttpResponseRedirect

def home(request):
    return render(request, "home.html",)

def about(request):
    return render(request, "about.html",)

def menu (request):
    return render(request, "menu.html",)

def team (request):
    return render(request, "team.html",)

def service (request):
    return render(request, "service.html",)

def testimonial (request):
    return render(request, "testimonial.html",)

def contact (request):
    return render(request, "contact.html",)

