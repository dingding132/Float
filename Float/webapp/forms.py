from django import forms

class SearchForm(forms.Form):
	departure = forms.CharField(label='departure', max_length=200)
	arrival = forms.CharField(label='arrival', max_length=200)
	date = forms.DateField(label='date')