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
def RandomTone():
    template_name = 'index.html'
    model = Item
    Tone = Item.objects.filter(id)

def RandomColour():
    template_name = 'Randomcolour.html'
    model = Item


class SearchItemListView(ListView):
    template_name = "item_search.html"
    model = Item

    def get_queryset(self):
        queryset = super(SearchItemListView, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            item_by_name = queryset.filter(name__icontains=q)
            item_by_category = queryset.filter(category__icontains=q)
            return item_by_name | item_by_category
        return queryset