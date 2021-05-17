from django.db import models


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    like_count = models.IntegerField(default=0)
    like_users = []

    def __str__(self):
        return self.title
