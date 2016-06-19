from django import forms

class SearchForm(forms.Form):
	departure = forms.CharField(label='Departure', max_length=200)
	arrival = forms.CharField(label='Arrival', max_length=200)
	date = forms.DateField(label='Date')