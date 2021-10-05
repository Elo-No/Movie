from django.db import models

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
