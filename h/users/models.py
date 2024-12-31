from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=15)
    dob=models.DateField(null=True, blank=True)
    Hospital_name =models.CharField(blank= True,max_length=100)

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    GENDER_CHOICES = [('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    symptoms = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name



