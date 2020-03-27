from django.shortcuts import render
from .models import CrawlerCovid
from django.views.generic import ListView, TemplateView


class CrawledListView(ListView):
    model = CrawlerCovid
    template_name = "crawledlist.html"

class Home(TemplateView):
    template_name = "home.html"