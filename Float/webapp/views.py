from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader

def index(request):
	template = loader.get_template('home.html')
	return HttpReponse(template.render(request))
def search_result(request):
	template = loader.get_template('search_results.html')
	return HttpReponse(template.render(request))

# Create your views here.
