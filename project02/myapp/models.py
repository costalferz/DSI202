from django.db import models
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    start = models.DateField(auto_now=False, auto_now_add=True)
    model = models.CharField(max_length=5)
    type  = models.CharField(max_length=20)
    year  = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "Car id:%s, start:%s model:%s type:%s year:%s price:%s"\
            %(self.id,self.start,self.model,self.type,self.year,self.price)
    def get_absolute_url(self):
        return reverse('car', args=[str(self.id)])