from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    post_id = models.PositiveIntegerField(primary_key=True, auto_created=True)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=10000)
    likes = models.PositiveIntegerField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.author} - {self.title} - {self.likes}"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.post_id} - {self.title}')
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)

