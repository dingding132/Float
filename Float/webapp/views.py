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
			#get search details
			departure = form.cleaned_data['departure']
			arrival = form.cleaned_data['arrival']
			date = form.cleaned_data['date']

			#get all trips
			trips = Trip()
			trips = Trip.objects.all()

			for trip in trips:
				distance_dict = gmaps.distance_matrix(trip.departure_city,trip.arrival_city)
				distance1 = distance_dict['rows'][0]['elements'][0]['distance']['value']
				trip.distance = distance1/1000
				trip.save

			#query trips 
	return render(request, 'search_result.html', {'trips': trips})

# Create your views here.


