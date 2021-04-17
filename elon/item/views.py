from django.shortcuts import render,redirect,reverse
import random
from django.db.models import Count
from django.contrib.auth.models import User
from django.views.generic import (DetailView,FormView,ListView,TemplateView,UpdateView)
from django.contrib.auth.decorators import login_required
from .models import (Item,itemHistory,Payment,Category)
# Create your views here.


def home(request):
    return render(request,'index.html')
class Random(ListView):
    template_name = 'index.html'
    model = Item
    color = Item.objects.filter(category=2) 