from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#from .views import *
from item import views
urlpatterns = [
    path('',views.home,name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
