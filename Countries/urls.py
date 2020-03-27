from django.urls import path
from .views import CountryList, CountryDetail, NewEntry

urlpatterns = [
    path('', CountryList.as_view(), name='countrylist'),
    path('<slug:slug>/', CountryDetail.as_view(), name='countrydetail'),
    path('add/entry', NewEntry.as_view(), name='newentry'),
]
