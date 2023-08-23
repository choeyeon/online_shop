from django.contrib import admin
from evapp.models import *
from django.contrib.admin import ModelAdmin


@admin.register(Goods)
class GoodsAdmin(ModelAdmin):
    pass
    

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    pass