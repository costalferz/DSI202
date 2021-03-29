from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    phone_num=models.CharField(max_length=10)
    age=models.CharField(max_length=3)
    career=models.CharField(max_length=100)
    business_size=models.CharField(max_length=30)
    interest=models.CharField(max_length=50)
    message=models.TextField(null=True)
    def __str__(self):
        return ("%s %s  %s <job>: %s  %s"%(self.id ,self.user.first_name, self.user.last_name, self.career,self.business_size))
    
class Designer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    skill=models.CharField(max_length=50)
    def __str__(self):
        return ("%s %s <skill> : %s "%(self.first_name, self.last_name, self.skill))

class Job(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    designer=models.ForeignKey(Designer, on_delete=models.CASCADE,null=True)
    package=models.CharField(max_length=100)
    cost=models.DecimalField(max_digits=10,decimal_places=0)
    customer_tell=models.TextField(null=True)
    def __str__(self):
        return ("customer:%s  Designer:%s Package:%s Cost:%s "%(self.customer, self.designer, self.package,self.cost))
