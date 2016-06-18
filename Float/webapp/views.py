from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader

def index(request):
	return render(request, 'home.html')
def search_result(request):
	return render(request, 'search_result.html')


# Create your views here.
