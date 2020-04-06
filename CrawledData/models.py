from django.contrib.gis.db import models

class Country(models.Model):
    name = models.CharField(max_length=50)
    pop2005 = models.IntegerField('Population 2005')
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    lon = models.FloatField()
    lat = models.FloatField()
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name

class CrawlerCovid(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    confirmed = models.IntegerField()
    active = models.IntegerField()
    new_cases = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    new_deaths = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country.name