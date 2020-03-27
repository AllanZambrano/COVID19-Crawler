from django import forms
from .models import CountryEntry
from flatpickr import DatePickerInput

class NewEntryForm(forms.ModelForm):
    class Meta:
        model = CountryEntry
        fields = ('country','state', 'date', 'new_cases', 'new_deaths', 'source')
        widgets = {
            'date': DatePickerInput(),
        }


