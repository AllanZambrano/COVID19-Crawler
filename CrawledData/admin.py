from django.contrib.gis import admin
from .models import CrawlerCovid, Country

class CountryAdmin(admin.GeoModelAdmin):
    list_display = ('name', 'pop2005', 'iso2', 'lat', 'lon')
    ordering = ['name']

class CrawlerAdmin(admin.ModelAdmin):
    list_display = ('country', 'confirmed', 'new_cases','deaths', 'new_deaths', 'updated_at')
    ordering = ['-confirmed']

admin.site.register(CrawlerCovid, CrawlerAdmin)
admin.site.register(Country, CountryAdmin)