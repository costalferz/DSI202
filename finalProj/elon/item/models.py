from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=30)
    slug = models.SlugField(unique=True,default=None)

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "หมวดหมู่"


class Item(models.Model):
    name = models.CharField(max_length=300)
    detail = models.TextField(max_length=1000)
    slug = models.SlugField(unique=True,default=None)
    img = models.ImageField(default='default_item.png', upload_to='item_pics')
    amount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,default=None)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)
        img = Image.open(self.img.path)

        if img.height > 200 or img.width > 200:
            output_size = (150, 300)
            img.thumbnail(output_size)
            img.save(self.img.path)
    
    class Meta:
        verbose_name_plural = "สินค้า"

class itemHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, editable=True)
    item = models.ForeignKey(Item, on_delete=models.PROTECT, editable=True)
    date = models.DateTimeField(auto_now_add=True)
    trackNum = models.CharField(max_length=15)
    class Meta:
        verbose_name_plural = "ประวัติการสั่งซื้อ"

class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.TextField(max_length=100,default="name")
    NumCard = models.CharField(max_length=13) 
    expire = models.DateField()
    cvv = models.CharField(max_length=3)
    class Meta:
        verbose_name_plural = "ระบบจ่ายเงิน"
