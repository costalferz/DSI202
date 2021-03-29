from django.contrib import admin
from .models import Customer,Designer,Job

class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','age','career','business_size','phone_num','interest','message']
    list_editable=['phone_num']
admin.site.register(Customer,CustomerAdmin)

class DesignerAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Designer._meta.fields]
    list_editable=['skill']
admin.site.register(Designer,DesignerAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Job._meta.fields]
    list_editable=['designer']
admin.site.register(Job,JobAdmin)
# admin.site.register(Property)
# admin.site.register(Rent)
# admin.site.register(Customer)
