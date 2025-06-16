from rest_framework import viewsets
from .models import Category
from category.serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer