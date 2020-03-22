from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Case

class HomeView(ListView):
    model = Case
    template_name = "home.html"