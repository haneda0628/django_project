from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Attendance(models.Model):
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=datetime.now)
