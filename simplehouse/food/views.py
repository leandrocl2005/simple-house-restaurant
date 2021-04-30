from .serializers import CategorySerializer, FoodSerializer
from .models import Category, Food
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


class ListCategories(generics.ListAPIView):

  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class ListFoods(generics.ListAPIView):

  queryset = Food.objects.all()
  serializer_class = FoodSerializer


class HomeFood(APIView):
  renderer_classes = [TemplateHTMLRenderer]
  template_name = 'index.html'

  def get(self, request):
    querysetCategory = Category.objects.all()
    querysetFood = Food.objects.all()
    return Response({'categories': querysetCategory, 'foods': querysetFood})
