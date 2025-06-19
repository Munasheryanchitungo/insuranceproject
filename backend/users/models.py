from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    BUSINESS_TYPES = [
        ('grocery', 'Grocery'),
        ('clothing', 'Clothing'),
        ('agriculture', 'Agriculture'),
        ('other', 'Other'),
    ]
    
    mobile = models.CharField(max_length=20)
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPES)
    
    def __str__(self):
        return self.username