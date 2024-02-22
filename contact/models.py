from django.db import models

# Create your models here.
class contact(models.Model):
    firstName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 200)
    emailId = models.EmailField(default=None)
    message = models.CharField(max_length = 500)