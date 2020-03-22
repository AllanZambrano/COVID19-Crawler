from django.contrib import admin
from .models import Case

class CaseAdmin(admin.ModelAdmin):
    list_display = ('country', 'total_cases', 'active_cases', 'total_deaths')
    ordering = ['-total_cases']
    search_fields = ['country']

admin.site.register(Case, CaseAdmin)

