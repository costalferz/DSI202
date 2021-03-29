from django.views.generic.detail import DetailView
from django.shortcuts import render,redirect
from myapp.models import Car
from django.http import HttpResponse


class CarDetailView(DetailView):
    model = Car
    template_name = 'car.html'