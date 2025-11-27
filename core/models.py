from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    preferences = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    # Encrypted fields would be better for passport, but for now simple charfield as per plan notes on security consideration
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
