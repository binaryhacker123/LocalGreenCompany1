from django.db import models
from django.contrib.auth.models import User
import json
# Create your models here.

class Feature (models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)


