from django.urls import path
from .views import CrawledListView, Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('crawled/', CrawledListView.as_view(), name='crawledlist'),
]
