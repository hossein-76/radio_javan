from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class SongCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'name:{self.name}, id:{self.id}'


class SongManager(models.Manager):
    def approved_songs(self):
        return self.filter(approval_status="approved")

    def exclusive_songs(self):
        return self.filter(approval_status="approved", is_exclusive=True)


class Song(models.Model):
    name = models.CharField(max_length=255)
    singer = models.ForeignKey(
        'art.Artist', on_delete=models.SET_NULL, null=True, blank=True)
    released_date = models.DateField()
    uploaded_date = models.DateTimeField(auto_now_add=True)
    song_file = models.FileField()
    is_exclusive = models.BooleanField(default=False)
    lyrics = models.TextField(blank=True)
    arrangement = models.ForeignKey(
        'art.Artist', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField(default=0)
    cover = models.ForeignKey(
        'art.Cover', on_delete=models.SET_NULL, null=True, blank=True)
    social_medias = JSONField(default=dict)
    tags = models.ManyToManyField('tag.Tag', blank=True)
    approval_status = models.CharField(max_length=50, choices=(
        ("approved", "approved"), ("pending", "pending"), ("rejected", "rejected")), default="pending")
    publish_status = models.CharField(max_length=255, choices=(
        ("comming_soon", "comming_soon"), ("published", "publshed"), ("rejected", "rejected")), default="comming_soon")
    objects = SongManager()

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'


class PlayList(models.Model):
    user = models.ForeignKey(
        'account.User', on_delete=models.CASCADE, related_name='play_lists')
    name = models.CharField(max_length=255, null=True, blank=True)
    songs = models.ManyToManyField(Song, blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'


class Album(models.Model):
    artist = models.ForeignKey(
        'art.Artist', on_delete=models.SET_NULL, null=True, blank=True)
    songs = models.ManyToManyField(Song, blank=True)
    name = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'


class SongView(models.Model):
    datetime = models.DateField()
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f'user:{self.user.id}, song:{self.song.id}'
