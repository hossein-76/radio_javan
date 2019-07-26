from django.db import models

# Create your models here.


class TagCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'


class Tag(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(TagCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'
