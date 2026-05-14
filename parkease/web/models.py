from django.db import models

# Create your models here.

class SignOut(models.Model):
    receiver_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=50)
