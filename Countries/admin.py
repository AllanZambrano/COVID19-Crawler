from django.contrib import admin
from .models import Country, State, CountryEntry
from django.utils.html import format_html

def confirm_source(modeladmin, request, queryset):
    for entry in queryset:
        entry.status = True
        entry.save()
    confirm_source.short_description = 'Confirm entry source'

class CountryEntryAdmin(admin.ModelAdmin):
    list_display = ('country', 'state', 'new_cases', 'new_deaths', 'status', 'date', 'source_url')
    list_filter = ['status', 'country']
    actions = [confirm_source, ]
    def source_url(self, obj):
        return format_html("<a href='{url}' target='_blank'>Source</a>", url=obj.source)

    source_url.short_description = "Source URL"

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)
    search_fields = ['name']

class StateAdmin(admin.ModelAdmin):
    list_display = ('country', 'name',)
    ordering = ['name']
    search_fields = ['name']

admin.site.register(CountryEntry, CountryEntryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)