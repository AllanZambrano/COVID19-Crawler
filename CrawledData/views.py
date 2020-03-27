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
        context['sum'] = CrawlerCovid.objects.all().aggregate(total_cases=Sum('confirmed'),
                                                              total_active=Sum('active'),
                                                              total_deaths=Sum('deaths')
                                                              )
        context['update'] = CrawlerCovid.objects.values("updated_at").order_by()[0]

        return context