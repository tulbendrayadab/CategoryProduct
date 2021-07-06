from rest_framework import serializers

from demo.models import Category, Product, ProductCategory


class CategorySerializer(serializers.ModelSerializer):
    """
        perform crud on categories
    """
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent']


class ProductSerializer(serializers.ModelSerializer):
    """
    perform crud on product
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class ProductCategoriesSerializer(serializers.ModelSerializer):
    """
    to create/update/delete the Product categories.
    """
    class Meta:
        model = ProductCategory
        fields = ['id', 'category', 'product']


class ProductCategoriesGetSerializer(serializers.ModelSerializer):
    """
    to view the Product categories with depth level one
    """
    class Meta:
        model = ProductCategory
        fields = ['id', 'category', 'product']
        depth = 1

