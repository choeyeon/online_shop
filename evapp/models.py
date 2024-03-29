from django.db import models
from django.contrib.auth.models import User


class Goods(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    desription = models.TextField()
    characteristics = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}, {self.price}'
    

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'
    

class Review(models.Model):
    RATING_CHOICES = (
        (None,'-'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    text = models.TextField()
    raiting = models.IntegerField(null=True, choices=RATING_CHOICES)
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE, null=False)



#TODO update or delete this
class ReviewLike(models.Model):
    rewiew = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(null=True)

    def save(self, *args, **kwargs):
                super().save(*args, **kwargs)
                self.review.likes_count = self.review.likes.filter(status=True).count()
                self.review.dislikes_count = self.review.likes.filter(status=False).count()
                self.review.save()


        
