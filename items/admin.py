from django.contrib import admin
from items.models import Category, ItemImage, LostItem, FoundItem
from accounts.models import User

# Register your models here.
admin.site.register(Category)
admin.site.register(ItemImage)
admin.site.register(LostItem)
admin.site.register(FoundItem)
admin.site.register(User)