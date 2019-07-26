from django.db import models

# Create your models here.


class ArtistManager(models.Manager):
    def get_active_artists(self):
        return self.filter(is_active=True)

    def get_verified_artists(self):
        return self.filter(is_verified=True)

    def get_active_verified_artists(self):
        return self.filter(is_active=True, is_verified=True)


class Artist(models.Model):
    name = models.CharField(max_length=50)
    admin = models.ForeignKey('account.User', on_delete=models.CASCADE)
    is_band = models.BooleanField(default=False)
    band_members = models.ManyToManyField('account.User', blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    art = models.CharField(max_length=100)
    # TODO: add choices to art later
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return super().__str__()

    def add_pop(self):
        self.popularity += 1
        self.save()


class Cover(models.Model):
    artist = models.ForeignKey(
        Artist, on_delete=models.SET_NULL, null=True, blank=True, related_name="covers")
    cover_file = models.FileField()

    def __str__(self):
        return f'id:{self.id}'
