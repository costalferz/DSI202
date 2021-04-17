from django.db import models
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.
SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unsure',),
)

class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    phone_num = models.CharField(max_length=10)
    img = models.ImageField(default='default.png', upload_to='profile_pices')
    sex = models.CharField(max_length=1,choices=SEX_CHOICES,)
    address = models.CharField(max_length=500,default=None)
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()
        img = Image.open(self.img.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.img.path)