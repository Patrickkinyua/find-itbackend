from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemImageViewSet, LostItemViewSet, FoundItemViewSet, CategoryViewSet
from items.views import FoundItemMatchView
router = DefaultRouter()
router.register(r'item-images', ItemImageViewSet , basename='itemimage')
router.register(r'lost-items', LostItemViewSet , basename='lostitem')
router.register(r'found-items', FoundItemViewSet , basename='founditem')
router.register(r'categories', CategoryViewSet , basename='category')

urlpatterns = [
    path('', include(router.urls)),
     path("match/found/<int:pk>/", FoundItemMatchView.as_view()),

]