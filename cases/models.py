from django.db import models

class Case(models.Model):
    country = models.CharField(max_length=150, primary_key=True)
    total_cases = models.IntegerField()
    active_cases = models.IntegerField()
    total_deaths =  models.IntegerField()

    def __str__(self):
        return self.country