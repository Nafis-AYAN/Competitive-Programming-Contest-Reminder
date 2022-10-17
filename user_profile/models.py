from django.db import models

# Create your models here.

class user_profile(models.Model):
    user_name = models.CharField(max_length=30)
    user_ID = models.IntegerField(primary_key = True, max_length=10)
    user_email = models.EmailField(max_length=20)
    user_password = models.CharField(max_length=20)
    contestSites_ID = models.CharField(max_length=20)
    user_contestSites = models.CharField(max_length=20)



