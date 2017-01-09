from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length = 200)
    post_number = models.CharField(max_length = 7)
    address = models.CharField(max_length = 200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=datetime.now)

USER_TYPE = (
             ('ADMIN', 'Admin'),
             ('EMPLOYEE', 'Employee'),
             )

class Employee(AbstractUser):
    company = models.ForeignKey(Company,related_name='jointed_company')
    post_number = models.CharField(max_length = 7)
    address = models.CharField(max_length = 200)


