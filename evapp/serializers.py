from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from evapp.models import *

class GoodsSerializer(ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GoodsUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    fullname = serializers.ReadOnlyField()


#TODO to reprezentation 
class ReviewGoodsSerializer(serializers.PrimaryKeyRelatedField):

    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return GoodsListSerializer(value, context=self.context).data



#TODO creatte update
class ReviewSerializer(ModelSerializer):
    like = serializers.IntegerField(read_only=True)
    dislike = serializers.IntegerField(read_only=True)
    goods = ReviewGoodsSerializer(read_only=True)
    user = GoodsUserSerializer(read_only=True)
    like_status = serializers.SerializerMethodField()

    def get_like_status(self, instance):
        user = self.context['request'].user
        if not user.is_anonymous:
            try:
                like = instance.likes.get(user=user)
                return like.status
            except models.ReviewLike.DoesNotExist:
                return None
        return None
    

    


    class Meta:
        model = Review
        fields = '__all__'


class GoodsListSerializer():
    title = serializers.CharField(read_only=True)
    price = serializers.FloatField(source='price', read_only=True)

    class Meta:
        model = Goods
        fields = '__all__'
