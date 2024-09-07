from rest_framework import serializers

from api.category.serializers import CategorySerializers

from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)
    category = CategorySerializers()

    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "image", "category")
