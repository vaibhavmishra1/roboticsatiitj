from django.db import models
COLOR_CHOICES = (
    ('B1','B1'),
    ('B2', 'B2'),
    ('B3','B3'),
    ('B5', 'B5'),
    ('G4', 'G4'),
    ('G5','G5'),
    ('G6','G6'),
	('I2', 'I2'),
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
	item=models.CharField(max_length=100)
	number=models.IntegerField()
	provided=models.BooleanField()


class MustKnowPeople(models.Model):
	name=models.CharField(max_length=100)
	year=models.IntegerField()
	description=models.CharField(max_length=500)
	contact=models.CharField(max_length=500)
	image1= models.ImageField(upload_to='images',blank=True)


