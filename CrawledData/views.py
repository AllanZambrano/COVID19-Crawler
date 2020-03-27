from .models import CrawlerCovid
from django.views.generic import ListView
from django.db.models import Sum

class CrawledListView(ListView):
    model = CrawlerCovid
    template_name = "crawledlist.html"

class Home(ListView):
    model = CrawlerCovid
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['sum'] = CrawlerCovid.objects.values('confirmed').aggregate(total_cases=Sum('confirmed'))

        return context