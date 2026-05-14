from django.db import models

# Create your models here.
class Vehicle(models.Model):
    VEHICLE_CHOICES = [
        ("truck","Truck"),
        ("boda_boda", "Boda Boda"),
        ("taxis","Taxis"),
        ("coaster", "Coaster"),
        ("personal_car", "Personal Car")

    ]

    driver_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    nin = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=255, choices=VEHICLE_CHOICES)
    number_plate = models.CharField(max_length=255)
    vehicle_model = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    arrival_time = models.DateTimeField(auto_now_add=True)
    parking_charge = models.DecimalField(max_digits=12, decimal_places=2)

class Receipt(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    receipt_number = models.CharField(max_length=255)
    issued_at = models.DateTimeField(auto_now_add=True)

