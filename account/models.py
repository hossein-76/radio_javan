from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import JSONField


class User(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True)
    like_songs = models.ManyToManyField(
        'music.Song', related_name='liked_songs', blank=True)
    liked_podcasts = models.ManyToManyField(
        'podcast.PodCast', related_name='liked_podcasts', blank=True)
    liked_videos = models.ManyToManyField(
        'video.Video', related_name='liked_videos', blank=True)
    follows = models.ManyToManyField("art.Artist", blank=True)

    def __str__(self):
        return f'username:{self.username},id:{self.id}'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='user_images')
    social_media = JSONField(default=dict)
    site = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'user:{self.user.username}, user_id:{self.user.id}'
