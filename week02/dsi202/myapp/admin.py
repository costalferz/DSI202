from django.contrib import admin
from myapp.models import Car, Customer, Rent

class CarAdmin(admin.ModelAdmin):
    list_display=['id','model','price','maker']
    list_editable=['price']
    list_filter=['maker']
    

class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','name', 'mobile']
    list_editable=['mobile']
    


class RentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Rent._meta.fields]
    list_editable=['cost']
    list_filter=['car']

admin.site.register(Car,CarAdmin)  
admin.site.register(Customer,CustomerAdmin)  
admin.site.register(Rent,RentAdmin)