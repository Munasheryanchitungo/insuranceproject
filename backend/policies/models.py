from django.db import models
from django.conf import settings

class Policy(models.Model):
    POLICY_TYPES = [
        ('fire', 'Fire Cover'),
        ('theft', 'Theft Protection'),
        ('comprehensive', 'Comprehensive'),
        ('health', 'Health Microinsurance'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=20, choices=POLICY_TYPES)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.get_policy_type_display()} Policy"