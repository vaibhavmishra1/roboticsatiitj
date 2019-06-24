from django.db import models
COLOR_CHOICES = (
    ('B1','B1'),
    ('B2', 'B2'),
    ('B3','B3'),
    ('G5','G5'),
    ('G6','G6'),
)
# Create your models here.
from django.contrib.auth.models import AbstractUser

class IITJUser(AbstractUser):
	contact=models.CharField(max_length=15)
	hostel = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')