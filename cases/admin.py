from django.contrib import admin
from .models import Case, Entry, Country

class CaseAdmin(admin.ModelAdmin):
    list_display = ('country', 'confirmed', 'active', 'deaths')
    ordering = ['-confirmed']
    search_fields = ['country__name']


class EntryAdmin(admin.ModelAdmin):
    pass

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)
    ordering = ['name']
    search_fields = ['name']

admin.site.register(Case, CaseAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Country, CountryAdmin)
