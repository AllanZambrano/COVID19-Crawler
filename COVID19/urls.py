from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('not-an-admin/', admin.site.urls),
    path('', include('CrawledData.urls')),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)),] + urlpatterns
