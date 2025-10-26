from django.db import models

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)

class Booking(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    No_of_guests=models.IntegerField()
    BookingDate=models.DateTimeField()

class Menu(models.Model):
    id=models.IntegerField(primary_key=True)
    Title=models.CharField(max_length=255)
    Price=models.DecimalField(max_digits=10,decimal_places=2)
    Inventory=models.IntegerField()
