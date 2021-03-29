from django.db import models

class Car(models.Model):
    maker = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    price = models.DecimalField(null=True, max_digits=10,decimal_places=2)
    def __str__(self):
        return "car_id:%s, model:%s"%(self.id,self.model)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    def __str__(self):
        return "customer_id:%s, name:%s"%(self.id,self.name)

class Rent(models.Model):
    car=models.ForeignKey('Car',on_delete=models.CASCADE)
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE)
    #on create
    rented_at=models.DateTimeField(auto_now=False, auto_now_add=True)
    #on update
    retruned_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    cost=models.DecimalField(blank=True, null=True, max_digits=10,decimal_places=2)
    def __str__(self):
        return "rent_id:%s"%(self.id)