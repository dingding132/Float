from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader
from array import array

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

			# #get all trips
			# trips = Trip()
			# trips = Trip.objects.all()

			#trips with only 1 connection
			trips1 = Trip()
			trips1 = Trip.objects.filter(departure_city=departure).filter(arrival_city=arrival).filter(departure_date=date)
			for trip in trips1:
				distance_dict = gmaps.distance_matrix(trip.departure_city,trip.arrival_city)
				distance1 = distance_dict['rows'][0]['elements'][0]['distance']['value']
				trip.distance = distance1/1000
				trip.save

			# #trips with 2 connections
			# firstTripID = []
			# secondTripID = []
			# trips2_departure_match = {"id", "driver","departure_date", "departure_time", "departure_city",
			# "arrival_city", "distance", "messages"}
			# trips2_arrival_match = {"id", "driver","departure_date", "departure_time", "departure_city",
			# "arrival_city", "distance", "messages"}
			# trips2_departure_match = Trip.objects.filter(departure_city=departure).values
			# trips2_arrival_match = Trip.objects.filter(arrival_city=arrival).values

			# for tripDeparture in trips2_departure_match:
			# 	for tripArrival in trips2_arrival_match:
			# 		if tripDeparture["arrival_city"] == tripArrival["departure_city"]:
			# 			firstTrip.append(tripDeparture["id"])
			# 			secondTrip.append(tripArrival["id"])

			# firstTrips = Trip()
			# secondTrips = Trip()

			# for i in firstTripID:
			# 	trip1 = Trip.objects.filter(id=firstTripID[i])
			# 	trip2 = Trip.objects.filter(id=secondTripID[i])
			# 	firstTrips.append(trip1)
			# 	secondTrips.append(trip2)


		 # #   #get distance from google api
			# # for trip in trips2FirstTrip:
			# # 	distance_dict = gmaps.distance_matrix(trip.departure_city,trip.arrival_city)
			# # 	distance1 = distance_dict['rows'][0]['elements'][0]['distance']['value']
			# # 	trip.distance = distance1/1000
			# # 	trip.save

			# # for trip in trips2SecondTrip:
			# # 	distance_dict = gmaps.distance_matrix(trip.departure_city,trip.arrival_city)
			# # 	distance1 = distance_dict['rows'][0]['elements'][0]['distance']['value']
			# # 	trip.distance = distance1/1000
			# # 	trip.save

			# #get total distance for 2 connections
			# # totalDistance2 = []
			# # for i in trips2SecondTrip.amount():
			# # 	distance = trips2FirstTrip[i].distance + trips2SecondTrip[i].distance
			# # 	totalDistance2.append(distance)

	return render(request, 'search_result.html', {'trips1': trips1})

# Create your views here.


