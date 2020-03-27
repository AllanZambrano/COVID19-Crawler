from django.db import models

class CrawlerCovid(models.Model):
    country = models.CharField(max_length=120)
    confirmed = models.PositiveIntegerField()
    active = models.PositiveIntegerField()
    new_cases = models.PositiveIntegerField(default=0)
    deaths = models.PositiveIntegerField(default=0)
    new_deaths = models.PositiveIntegerField(default=0)
    recovered = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country