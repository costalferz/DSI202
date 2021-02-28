from django.views.generic.detail import DetailView
from django.shortcuts import render,redirect
from myapp.models import Car
from django.http import HttpResponse
# Create your views here.
class CarDetailView(DetailView):
    model = Car
    template_name = 'car.html'