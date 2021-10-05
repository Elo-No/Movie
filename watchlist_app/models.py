from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField(max_length=200)
    website = models.URLField(max_length=4000)
    
    def __str__(self):
        return self.name

class Watchlist(models.Model):
    title = models.CharField(max_length=200)
    story_line = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchlist")

    def __str__(self):
        return self.title

class Review(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    Watchlist = models.ForeignKey(Watchlist,on_delete=models.CASCADE,related_name="review")

    def __str__(self):
        return str(self.rating) + "-" + self.Watchlist.title
