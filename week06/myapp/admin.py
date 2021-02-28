from django.contrib import admin
from myapp.models import Car,Bike

class BikeAdmin(admin.ModelAdmin):
    list_display=['id','start','type','price']
class CarAdmin(admin.ModelAdmin):
    list_display=['id','start','model','type','year','price']
admin.site.register(Bike, BikeAdmin)
admin.site.register(Car, CarAdmin)