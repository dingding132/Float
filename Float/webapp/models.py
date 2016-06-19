from django.db import models

class Driver(models.Model):
	id =  models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	picture = models.CharField(max_length=200)
	car_make = models.CharField(max_length=50)
	car_year = models.IntegerField()

class Trip(models.Model):
	id =  models.AutoField(primary_key=True)
	driver = models.ForeignKey(Driver)
	departure_date = models.DateField()
	departure_time = models.TimeField()
	departure_city = models.CharField(max_length=200)
	arrival_city = models.CharField(max_length=200)


