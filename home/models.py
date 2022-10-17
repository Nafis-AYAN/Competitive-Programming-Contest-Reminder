from tkinter import CASCADE
from django.db import models

from user_profile.models import user_profile



# Create your models here.

class home(models.Model):

    user_contestSites = models.ForeignKey(user_profile, on_delete=models.CASCADE)
    contest_name = models.CharField(max_length=20)
    contest_date = models.IntegerField(max_length=10)
    contest_url=models.URLField(primary_key=True, max_length=50)

