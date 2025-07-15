from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(help_text="Enter a valid email address")
    contact = models.CharField(max_length=10)
    date_registered = models.DateField(auto_now_add=True)