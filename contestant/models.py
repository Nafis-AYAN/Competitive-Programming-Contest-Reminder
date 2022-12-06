import imp
from django.db import models

from django.contrib.auth.models import User



# Create your models here.

class contestant(models.Model):
    c_id = models.IntegerField(primary_key = True)
    c_photo = models.ImageField(upload_to='', default = 'default.png')
    dateOfBirth = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
