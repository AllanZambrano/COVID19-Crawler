from django.db import models

class CrawlerCovid(models.Model):
    country = models.CharField(max_length=120)
    confirmed = models.IntegerField()
    active = models.IntegerField()
    new_cases = models.IntegerField(default=0)
    deaths = models.PositiveIntegerField(default=0)
    new_deaths = models.PositiveIntegerField(default=0)
    recovered = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country