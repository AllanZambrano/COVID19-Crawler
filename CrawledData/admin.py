from django.contrib import admin
from .models import CrawlerCovid

class CrawlerAdmin(admin.ModelAdmin):
    list_display = ('country', 'confirmed', 'new_cases','deaths', 'new_deaths', 'updated_at')
    ordering = ['-confirmed']

admin.site.register(CrawlerCovid, CrawlerAdmin)