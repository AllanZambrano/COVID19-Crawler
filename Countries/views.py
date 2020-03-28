from .models import Country, CountryEntry
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.db.models import Sum, Window, F
from .forms import NewEntryForm
from django.urls import reverse_lazy


class CountryList(ListView):
    model = Country
    template_name = 'countrylist.html'


class CountryDetail(DetailView):
    model = Country
    template_name = 'countrydetail.html'

    def get_context_data(self, **kwargs):
        context = super(CountryDetail, self).get_context_data(**kwargs)
        context['labels'] = CountryEntry.objects.filter(country__name=self.object, status=True).values("date").annotate(
            sum_cases=Sum("new_cases")).order_by()
        context['total'] = CountryEntry.objects.filter(country__name=self.object).aggregate(
            total_cases=Sum("new_cases"),
            total_deaths=Sum("new_deaths"),
        )
        context['cum_sum'] = CountryEntry.objects.filter(country__name=self.object).annotate(
            cumsum=Window(Sum('new_cases'), order_by=F("date").asc())).order_by("date",'cumsum').values("date", "cumsum").distinct()

        return context


class NewEntry(CreateView):
    template_name = 'new_entry.html'
    form_class = NewEntryForm
    success_url = reverse_lazy('countrylist')
