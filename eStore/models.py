from django.db import models
from django.db.models.base import Model

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField( max_length=254)
    phonenumber = models.CharField(max_length=12)
    device = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.phonenumber}"


class Fault(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    number = models.IntegerField()
    fault = models.ForeignKey(Fault, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.number}______{self.customer.name}______{self.customer.device}______{self.status}______{self.date}"

