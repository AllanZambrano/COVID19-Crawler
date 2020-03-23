from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=150, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"

class Entry(models.Model):
    case = models.ForeignKey('Case', on_delete=models.CASCADE)
    new_cases = models.PositiveIntegerField(default=0)
    new_deaths = models.PositiveIntegerField(default=0)
    SOURCE_STATUS = (
            ('WA', 'Waiting Approval'),
            ('A', 'Approved'),
            ('R', 'Rejected'),
        )
    status = models.CharField(
        max_length=2,
        choices=SOURCE_STATUS,
        blank=True,
        default='WA',
        help_text='Source Status',
    )
    source = models.URLField()
    comment = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.case.country

class Case(models.Model):
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    confirmed = models.PositiveIntegerField(default=0)
    active = models.PositiveIntegerField(default=0)
    new_cases = models.PositiveIntegerField(default=0)
    deaths =  models.PositiveIntegerField(default=0)
    new_deaths = models.PositiveIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country