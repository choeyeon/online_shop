from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from evapp.models import *
from evapp.serializers import *
from rest_framework import generics, mixins, viewsets
from drf_yasg.utils import swagger_auto_schema


class GoodsViewSet(ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserReviewListViewSet(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by('-id')
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        user = self.get_object()
        queryset = self.filter_queryset(self.get_queryset().filter(user=user))


class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    @swagger_auto_schema(tags=['Review'], operation_description='PUT /review/{id}/', operation_summary='Update review')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Review'], operation_description='PATCH /review/{id}/', operation_summary='Partial update review')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Review'], operation_description='DELETE /review/{id}/', operation_summary='Delete review')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Review'], operation_description='POST /review/', operation_summary='Write review')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)



    

