from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import ItemImage, LostItem, FoundItem, Category
from .serializers import CategorySerializer, ItemImageSerializer, LostItemSerializer, FoundItemSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import filters
from rest_framework.views import APIView
from items.services.matching_service import match_found_to_lost

from items import serializers


# Create your views here.
class ItemImageViewSet(viewsets.ModelViewSet):
    queryset = ItemImage.objects.all()
    serializer_class = ItemImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LostItemViewSet(viewsets.ModelViewSet):
    queryset = LostItem.objects.all().order_by('-created_at')
    serializer_class = LostItemSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'location', 'category__name']
    ordering_fields = ['date_lost', 'created_at']

class FoundItemViewSet(viewsets.ModelViewSet):
    queryset = FoundItem.objects.all().order_by('-created_at')
    serializer_class = FoundItemSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'location', 'category__name']
    ordering_fields = ['date_found', 'created_at']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    class Meta:
        model = Category
        fields = ['id', 'name']

class FoundItemMatchView(APIView):
    def get(self, request, pk):
        try:
            found_item = FoundItem.objects.get(pk=pk)
        except FoundItem.DoesNotExist:
            return Response(
                {"detail": "Found item not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        matches = match_found_to_lost(found_item)

        response = [
            {
                "lost_item_id": m["lost_item"].id,
                "title": m["lost_item"].title,
                "score": m["score"]
            }
            for m in matches
        ]

        return Response(response, status=status.HTTP_200_OK)