from django.db import models

from asd.utils import autoslug


@autoslug('title')
class Category(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
