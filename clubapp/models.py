from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Membership(models.Model):
    MEMBERSHIP_CHOICES = [
        ('Regular', 'Regular'),
        ('VIP', 'VIP'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, default='Regular')
    start_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.membership_type}"


# Create your models here.
