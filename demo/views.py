from rest_framework import viewsets

from demo.models import Category, Product, ProductCategory
from demo.serializers import (CategorySerializer, ProductSerializer, ProductCategoriesSerializer,
                              ProductCategoriesGetSerializer)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing category products.
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoriesSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductCategoriesGetSerializer
        return ProductCategoriesSerializer
