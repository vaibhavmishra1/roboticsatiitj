from django.db import models
COLOR_CHOICES = (
    ('B1','B1'),
    ('B2', 'B2'),
    ('B3','B3'),
    ('G5','G5'),
    ('G6','G6'),
)
STATUS_CHOICES = (
    ('ONGOING','ongoing'),
    ('COMPLETED', 'completed'),
    
)
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
class IITJUser(AbstractUser):
	contact=models.CharField(max_length=15)
	hostel = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')

class Project(models.Model):
	user=models.ForeignKey(IITJUser,on_delete=models.CASCADE)
	topic=models.CharField(max_length=200)
	description=models.CharField(max_length=5000)
	number_of_members_required=models.IntegerField()
	status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')


class Feedback(models.Model):
	user=models.ForeignKey(IITJUser,on_delete=models.CASCADE)
	description=models.CharField(max_length=5000)

class IssueMaterial(models.Model):
	user=models.ForeignKey(IITJUser,on_delete=models.CASCADE)
	