from django.views.generic.detail import DetailView
from django.shortcuts import render,redirect
from myapp.models import Bike,Car
from django.http import HttpResponse


class BikeDetailView(DetailView):
    model = Bike
    template_name = 'bike_detail.html'
class CarDetailView(DetailView):
    model = Car
    template_name = 'car.html'