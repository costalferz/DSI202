from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category
    

class Item(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=300)
    detail = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    img = models.ImageField(default='default_item.png', upload_to='item_pics')
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class itemHistory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)
