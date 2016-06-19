from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader

from webapp.forms import SearchForm
from webapp.models import Driver
from webapp.models import Trip
import googlemaps

gmaps = googlemaps.Client (key='AIzaSyBP7mNqXolKjnn1XJQnf58SHq_w3_qahqs')

def index(request):
	return render(request, 'home.html')

def search_result(request):
	if request.method == 'GET':
		return render(request,'search_result.html')
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			trips = Trip()
			departure = form.cleaned_data['departure']
			arrival = form.cleaned_data['arrival']
			date = form.cleaned_data['date']
			distance_dict = gmaps.distance_matrix(departure,arrival)
			distance1 = distance_dict['rows'][0]['elements'][0]['distance']['value']
			#query trips 
			trips = Trip.objects.filter(departure_city=departure).filter(arrival_city=arrival).filter(departure_date=date)
	return render(request, 'search_result.html', {'trips': trips})

# Create your views here.


