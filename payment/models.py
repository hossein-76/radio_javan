from django.db import models

# Create your models here.


class Donate(models.Model):
    from_user = models.ForeignKey(
        "account.User", on_delete=models.SET_NULL, null=True, blank=True)
    to_artist = models.ForeignKey(
        "art.Artist", on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.FloatField()

    def __str__(self):
        return f'id:{self.id}'
