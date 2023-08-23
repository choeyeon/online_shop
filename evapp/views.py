from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from evapp.models import *
from evapp.serializers import *
from rest_framework import generics


class GoodsViewSet(ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewViewSet(generics.GenericsApiView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
