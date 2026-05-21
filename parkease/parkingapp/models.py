from django.db import models
from django.utils import timezone
from datetime import time

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

    def calculate_parking_charge(self,duration_hours = 0):
        arrival = (self.arrival_time or timezone.now()).time()
        is_day = time(6,0) <= arrival <= time(18,59)


## This is for the duration
        if duration_hours < 3:
            if self.vehicle_type == "truck":
                return 2000
            elif self.vehicle_type == "personal_car":
                return 2000
            elif self.vehicle_type == "taxis":
                return 2000
            elif self.vehicle_type == "coaster":
                return 3000
            elif self.vehicle_type == "boda_boda":
                return 1000
            
## Day and Night charges

        if self.vehicle_type == "truck":
            return 5000 if is_day else 10000
        elif self.vehicle_type == "personal_car":
            return 3000 if is_day else 2000
        elif self.vehicle_type == "taxis":
            return 3000 if is_day else 2000
        elif self.vehicle_type == "coaster":
            return 4000 if is_day else 2000
        elif self.vehicle_type == "boda_boda":
            return 2000 
        return 0
    def save(self, *args, **kwargs):
        self.parking_charge = self.calculate_parking_charge()
        super().save(*args, **kwargs)





class Receipt(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    receipt_number = models.CharField(max_length=255)
    issued_at = models.DateTimeField(auto_now_add=True)

