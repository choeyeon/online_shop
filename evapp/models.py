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
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    score = models.FloatField(null=True)

    def set_score(self):
        likes_count = self.likes or 1
        dislikes_count = self.dislikes or 1
        rating = self.rating or 1
        self.score = (likes_count / dislikes_count) * (1 / rating)

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


        
