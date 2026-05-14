from django import forms
from parkingapp.models import Vehicle
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields= [
    "driver_name", 
    "phone_number", 
    "nin",
    "vehicle_type",
    "number_plate", 
    "vehicle_model", 
    "color",
    "parking_charge"
]

