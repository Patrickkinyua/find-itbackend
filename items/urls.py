from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemImageViewSet, LostItemViewSet, FoundItemViewSet, CategoryViewSet
router = DefaultRouter()
router.register(r'item-images', ItemImageViewSet , basename='itemimage')
router.register(r'lost-items', LostItemViewSet , basename='lostitem')
router.register(r'found-items', FoundItemViewSet , basename='founditem')
router.register(r'categories', CategoryViewSet , basename='category')

urlpatterns = [
    path('', include(router.urls)),
]