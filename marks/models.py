from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=100)
    roll= models.IntegerField()
    subject1= models.IntegerField()
    subject2= models.IntegerField()
    subject3= models.IntegerField()

    def total(self):
        return self.subject1 + self.subject2+ self.subject3

    def percentage(self):
        return self.total()/3
    
    def __str__(self):
        return self.name

class Profile(models.Model):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username