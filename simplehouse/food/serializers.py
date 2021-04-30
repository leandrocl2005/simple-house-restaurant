from rest_framework.serializers import ModelSerializer
from .models import Category, Food


class FoodSerializer(ModelSerializer):
  class Meta:
    model = Food
    fields = ('id', 'name', 'description', 'photo', 'price', 'category',
              'formatted_price')
    extra_kwargs = {'formatted_price': {'read_only': True}}


class CategorySerializer(ModelSerializer):

  food = FoodSerializer(many=True, read_only=True)

  class Meta:
    model = Category
    fields = ('id', 'name', 'food')