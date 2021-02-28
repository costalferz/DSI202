from django.contrib import admin
from myapp.models import Car

class CarAdmin(admin.ModelAdmin):
    list_display=['id','start','model','type','year','price']
admin.site.register(Car, CarAdmin)