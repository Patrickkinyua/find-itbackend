from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, default='')
    location = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    rating = models.FloatField(default=0.0)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return self.email
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    preffered_contact_method = models.CharField(max_length=50, blank=True, null=True, choices=[('email', 'Email'), ('phone', 'Phone'), ('in_app', 'In-App')]) 
    email_notifications = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.user.email}'s Profile"    