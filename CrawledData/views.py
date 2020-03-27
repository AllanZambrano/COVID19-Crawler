from django.shortcuts import render
from .models import CrawlerCovid
from django.views.generic import ListView, TemplateView
from django.db.models import Sum

class CrawledListView(ListView):
    model = CrawlerCovid
    template_name = "crawledlist.html"

class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['total'] = CrawlerCovid.objects.aggregate(sum_cases=Sum("confirmed"),
                                                          sum_active=Sum("active"),
                                                          sum_deaths=Sum("deaths"))
        context['update'] = CrawlerCovid.objects.values("updated_at").order_by()[0]
        return context
