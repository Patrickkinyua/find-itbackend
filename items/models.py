from django.db import models
from django.conf import settings


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, default='General')

    def __str__(self):
        return self.name
    
class ItemImage(models.Model):
    image = models.ImageField(upload_to='item_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url
class LostItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=255)
    date_lost = models.DateField()
    images = models.ManyToManyField(ItemImage, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='lost')  # lost or found

    def __str__(self):
        return self.title 
    
class FoundItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=255)
    date_found = models.DateField()
    images = models.ManyToManyField(ItemImage, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='found')  # lost or found

    def __str__(self):
        return self.title

