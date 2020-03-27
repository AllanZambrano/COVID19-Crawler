from django.db import models
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('country_detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Countries"


class State(models.Model):
    name = models.CharField(max_length=150, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CountryEntry(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField()
    new_cases = models.PositiveIntegerField(default=0)
    new_deaths = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    source = models.URLField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.country.name

    @property
    def total_active(self):
        return self.new_cases - self.new_deaths
